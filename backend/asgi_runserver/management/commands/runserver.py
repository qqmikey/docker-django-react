import errno
import os
import sys
import uvicorn
from datetime import datetime

from django.conf import settings
from django.contrib.staticfiles.handlers import ASGIStaticFilesHandler
from django.contrib.staticfiles.management.commands import runserver
from django.core.asgi import get_asgi_application
from django.core.exceptions import ImproperlyConfigured
from django.core.servers.basehttp import run
from django.utils import autoreload
from django.utils.module_loading import import_string


class Command(runserver.Command):
    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument(
            "--asgi",
            action="store_true",
            dest="asgi",
            help="Run an ASGI-based runserver rather than the WSGI-based one",
        )

    def inner_run(self, *args, **options):
        # If an exception was silenced in ManagementUtility.execute in order
        # to be raised in the child process, raise it now.
        autoreload.raise_last_exception()

        # 'shutdown_message' is a stealth option.
        shutdown_message = options.get("shutdown_message", "")
        quit_command = "CTRL-BREAK" if sys.platform == "win32" else "CONTROL-C"

        if not options["skip_checks"]:
            self.stdout.write("Performing system checks...\n\n")
            self.check(display_num_errors=True)
        # Need to check migrations here, so can't use the
        # requires_migrations_check attribute.
        self.check_migrations()
        now = datetime.now().strftime("%B %d, %Y - %X")
        self.stdout.write(now)
        self.stdout.write(
            (
                "Django version %(version)s, using settings %(settings)r\n"
                "Starting development server at %(protocol)s://%(addr)s:%(port)s/\n"
                "Quit the server with %(quit_command)s."
            )
            % {
                "version": self.get_version(),
                "settings": settings.SETTINGS_MODULE,
                "protocol": self.protocol,
                "addr": "[%s]" % self.addr if self._raw_ipv6 else self.addr,
                "port": self.port,
                "quit_command": quit_command,
            }
        )

        try:
            self.run_server(*args, **options)
        except OSError as e:
            # Use helpful error messages instead of ugly tracebacks.
            ERRORS = {
                errno.EACCES: "You don't have permission to access that port.",
                errno.EADDRINUSE: "That port is already in use.",
                errno.EADDRNOTAVAIL: "That IP address can't be assigned to.",
            }
            try:
                error_text = ERRORS[e.errno]
            except KeyError:
                error_text = e
            self.stderr.write("Error: %s" % error_text)
            # Need to use an OS exit because sys.exit doesn't work in a thread
            os._exit(1)
        except KeyboardInterrupt:
            if shutdown_message:
                self.stdout.write(shutdown_message)
            sys.exit(0)

    def get_handler(self, *args, **options):
        if not options["asgi"]:
            return super().get_handler(*args, **options)

        handler = get_internal_asgi_application()
        use_static_handler = options["use_static_handler"]
        insecure_serving = options["insecure_serving"]
        if use_static_handler and (settings.DEBUG or insecure_serving):
            return ASGIStaticFilesHandler(handler)
        return handler

    def run_server(self, *args, **options):
        if not options["asgi"]:
            self.run_wsgi_server(*args, **options)
        else:
            self.run_asgi_server(*args, **options)

    def run_wsgi_server(self, *args, **options):
        threading = options["use_threading"]
        handler = self.get_handler(*args, **options)
        run(
            self.addr,
            int(self.port),
            handler,
            ipv6=self.use_ipv6,
            threading=threading,
            server_cls=self.server_cls,
        )

    def run_asgi_server(self, *args, **options):
        handler = self.get_handler(*args, **options)
        uvicorn.run(
            handler,
            host=self.addr,
            port=int(self.port),
            log_level="info"
        )


def get_internal_asgi_application():
    """
    Load and return the WSGI application as configured by the user in
    ``settings.ASGI_APPLICATION``. With the default ``startproject`` layout,
    this will be the ``application`` object in ``projectname/asgi.py``.

    This function, and the ``ASGI_APPLICATION`` setting itself, are only useful
    for Django's internal server (runserver); external ASGI servers should just
    be configured to point to the correct application object directly.

    If settings.ASGI_APPLICATION is not set (is ``None``), return
    whatever ``django.core.asgi.get_asgi_application`` returns.
    """
    from django.conf import settings

    app_path = getattr(settings, "ASGI_APPLICATION", None)
    if app_path is None:
        return get_asgi_application()

    try:
        return import_string(app_path)
    except ImportError as err:
        raise ImproperlyConfigured(
            "ASGI application '%s' could not be loaded; "
            "Error importing module." % app_path
        ) from err

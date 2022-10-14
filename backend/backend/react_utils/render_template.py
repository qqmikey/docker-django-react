from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponse
from django.template import engines
from django.template.autoreload import reset_loaders
from django.template.backends.django import DjangoTemplates
from django.template.response import TemplateResponse
from django.views import View
from rest_framework import status

from backend.react_utils.web_server_propxy import web_server_proxy


class FrontendTemplateView(View):
    def get_initial_data(self, **kwargs):
        return {}

    def get_context_data(self, **kwargs):
        context = {
            'initial_data': self.get_initial_data(**kwargs),
        }
        return context

    def get(self, request, *args, **kwargs):
        ctx = self.get_context_data(**kwargs)
        return render_frontend_template(request, ctx)


def render_frontend_template(request, context=None, from_web_server=False):
    template = 'index.html'
    if settings.DEBUG or from_web_server:
        return web_server_proxy(request, context, templates=get_backend_template(), path=template)
    return TemplateResponse(request, template, context)


def get_backend_template():
    for engine in engines.all():
        if isinstance(engine, DjangoTemplates):
            return engine
    raise ImproperlyConfigured("No DjangoTemplates backend is configured.")


def reset_templates_cache():
    reset_loaders()


def clear_templates_cache_view(request):
    if request.GET.get('secret') != settings.SECRET_KEY:
        return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
    reset_templates_cache()
    return HttpResponse()

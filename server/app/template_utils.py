from urllib.request import urlopen

from django.http import HttpResponse


def render_str_template(request, template, context=None, content_type=None, status=None):
    t = get_backend_template().from_string(template.decode())
    content = t.render(context, request)
    return HttpResponse(content, content_type, status)


def fetch_frontend_template():
    response = urlopen('http://frontend:3000')
    content = response.read()
    return content


def get_backend_template():
    from django.template import engines
    from django.template.backends.django import DjangoTemplates
    for engine in engines.all():
        if isinstance(engine, DjangoTemplates):
            return engine
    return None


def reset_template_cache():
    from django.template.loader import engines
    for engine in engines.all():
        engine.engine.template_loaders[0].reset()

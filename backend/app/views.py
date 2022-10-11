from django.conf import settings
from django.shortcuts import render

from .template_utils import render_str_template, fetch_frontend_template


def main(request):
    ctx = {
        'scripts': [],
        'styles': [
            'https://fonts.googleapis.com/css?family=Roboto:300,400,500',
            'https://fonts.googleapis.com/icon?family=Material+Icons',
        ],
    }

    if not settings.DEBUG:
        return render(request, 'index.html', ctx)
    return render_str_template(request, fetch_frontend_template(), ctx)

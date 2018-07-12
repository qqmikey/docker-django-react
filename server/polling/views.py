from django.shortcuts import render
from django.conf import settings


def main(request):
    ctx = {
        'scripts': [],
        'styles': [
            'https://fonts.googleapis.com/css?family=Roboto:300,400,500',
            'https://fonts.googleapis.com/icon?family=Material+Icons'
        ],
    }

    if settings.DEBUG:
        ctx['scripts'].append('http://localhost:8080/hotreload/bundle.js')
    else:
        ctx['scripts'].append('/static/react/bundle.js')
    return render(request, 'main.html', ctx)

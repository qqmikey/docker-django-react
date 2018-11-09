from django.shortcuts import render


def main(request):
    ctx = {
        'scripts': ['/static/dist/bundle.js'],
        'styles': [
            'https://fonts.googleapis.com/css?family=Roboto:300,400,500',
            'https://fonts.googleapis.com/icon?family=Material+Icons',
            '/static/dist/bundle.css'
        ],
    }

    return render(request, 'main.html', ctx)

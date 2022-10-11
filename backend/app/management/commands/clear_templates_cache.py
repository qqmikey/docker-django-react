from urllib.parse import urlencode
from urllib.request import urlopen

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        # TODO: refactor clear template loader cache without request
        secret = settings.SECRET_KEY
        query = urlencode({'secret': secret})
        response = urlopen(f'http://backend:8000/api/v1/clear_template_cache?{query}')
        self.stdout.write('success.' if response.code == 200 else 'error.')

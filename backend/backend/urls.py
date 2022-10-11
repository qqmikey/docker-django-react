from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from app.template_utils import clear_template_cache_view
from app.views import main

urlpatterns = [
    path('', main),
    path('admin/', admin.site.urls),
    path('api/v1/clear_template_cache', clear_template_cache_view),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns

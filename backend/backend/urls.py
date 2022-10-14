from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from app import page_views as pages
from backend.react_utils.render_template import clear_templates_cache_view

urlpatterns = [
    path('', pages.HomePageView.as_view(), name='home_page'),
    # re_path('^login/?$', pages.LoginPageView.as_view(), name='login_page'),
    # re_path('^logout/?$', pages.LogoutPageView.as_view(), name='logout_page'),
    path('admin/', admin.site.urls),
    path('api/v1/clear_template_cache', clear_templates_cache_view),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns

from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.views import RedirectURLMixin
from django.http import HttpResponseRedirect
from django.shortcuts import resolve_url
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

from backend.react_utils.render_template import FrontendTemplateView


class LoginRequiredMixin(AccessMixin):
    only_authenticated = True

    def dispatch(self, request, *args, **kwargs):
        if self.only_authenticated and not request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class LoginPageView(RedirectURLMixin, FrontendTemplateView):
    redirect_authenticated_user = True
    next_page = 'home_page'

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if self.redirect_authenticated_user and request.user.is_authenticated:
            redirect_to = self.get_success_url()
            if redirect_to == self.request.path:
                raise ValueError(
                    "Redirection loop for authenticated user detected. Check that "
                    "your LOGIN_REDIRECT_URL doesn't point to a login page."
                )
            return HttpResponseRedirect(redirect_to)
        return super().dispatch(request, *args, **kwargs)

    def get_default_redirect_url(self):
        if self.next_page:
            return resolve_url(self.next_page)
        return resolve_url(settings.LOGIN_REDIRECT_URL)


class LogoutPageView(RedirectURLMixin, FrontendTemplateView):
    next_page = 'home_page'

    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        """Logout may be done via POST."""
        logout(request)
        redirect_to = self.get_success_url()
        if redirect_to != request.get_full_path():
            return HttpResponseRedirect(redirect_to)
        return super().get(request, *args, **kwargs)

    def get_default_redirect_url(self):
        if self.next_page:
            return resolve_url(self.next_page)
        if settings.LOGOUT_REDIRECT_URL:
            return resolve_url(settings.LOGOUT_REDIRECT_URL)
        return self.request.path


class HomePageView(LoginRequiredMixin, FrontendTemplateView):
    only_authenticated = False
    login_url = 'login_page'

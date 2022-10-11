from django.conf import settings
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .template_utils import render_str_template, fetch_frontend_template


class BasePageView(View):
    ONLY_AUTHENTICATED = False

    def get_initial_data(self, **kwargs):
        return {}

    def get_context_data(self, **kwargs):
        context = {
            'initial_data': self.get_initial_data(**kwargs),
        }
        return context

    def get(self, request, *args, **kwargs):
        if self.ONLY_AUTHENTICATED and not request.user.is_authenticated:
            return redirect(reverse('login_page'))

        ctx = self.get_context_data(**kwargs)

        if not settings.DEBUG:
            return render(request, 'index.html', ctx)
        return render_str_template(request, fetch_frontend_template(), ctx)


class LoginPageView(BasePageView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('home_page'))
        return super().get(request, *args, **kwargs)


class LogoutPageView(BasePageView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        return redirect(reverse('login_page'))


class HomePageView(BasePageView):
    ONLY_AUTHENTICATED = False

from django.views.generic import View, TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class LoginRequired(LoginRequiredMixin):
    login_url = "/login/"

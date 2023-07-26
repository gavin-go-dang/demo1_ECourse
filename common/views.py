from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, View

# Create your views here.


class LoginRequired(LoginRequiredMixin):
    login_url = "/login/"

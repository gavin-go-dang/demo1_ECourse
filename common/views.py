from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, View
from django.views.generic.detail import DetailView

# Create your views here.


class LoginRequired(LoginRequiredMixin):
    login_url = "/login/"


class DetailLoginRequired(LoginRequired, DetailView):
    pass

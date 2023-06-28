from django.views.generic import View, TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class LoginRequire(LoginRequiredMixin):
    login_url = "../../login"

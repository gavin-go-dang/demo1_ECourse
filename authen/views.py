from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User, auth
from django.views import View
from django.views.generic import View, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from .models import User
from django.contrib.auth import get_user_model
from .forms import SignUpForm

# Create your views here.


class HomeView(View):
    template_name = "index.html"

    def get(self, request):
        return render(request, self.template_name)


class LogoutView(LogoutView):
    next_page = "home"


class LoginView(LoginView):
    template_name = "login.html"
    success_url = ""

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return super().dispatch(request, *args, **kwargs)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password")
        return super().form_invalid(form)

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect("home")


class RegisterView(View):
    template_name = "registeration.html"
    title = "Register"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home")
        context = {"title": self.title, "message": ""}
        return render(request, self.template_name, context)

    def post(self, request):
        form = SignUpForm(request.POST)
        # error = " ".join([" ".join(x for x in l) for l in list(form.errors.values())])
        error = " ".join([x for l in form.errors.values() for x in l])
        if not form.is_valid():
            context = {"message": error}
            return render(request, "registeration.html", context)
        form.create_user()
        if form.cleaned_data["type"] == "student":
            return redirect("login")
        else:
            return redirect("../admin")

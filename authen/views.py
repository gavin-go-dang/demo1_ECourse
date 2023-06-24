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

# Create your views here.


class HomeView(TemplateView):
    template_name = "index.html"


class MyLogoutView(LogoutView):
    next_page = "home"


class MyLoginView(LoginView):
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

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home")
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST["username"]
        fullname = request.POST["fullname"]
        email = request.POST["email"]
        type = request.POST["role"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:
            if User.objects.filter(username=username):
                messages.info(request, "Your name has existed")
                return redirect("register")

            elif User.objects.filter(email=email):
                messages.info(request, "Your email has been used")

                return redirect(register)

            else:
                user = User.objects.create_user(
                    username=username, password=password, email=email, type=type
                )
                user.save()
                if type == "student":
                    return redirect("login")
                else:
                    return redirect("../admin")

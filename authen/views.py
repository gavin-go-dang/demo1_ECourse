from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User, auth
from django.views.generic import View, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from .models import User
from django.contrib.auth import get_user_model
from .forms import SignUpForm
from course_manager.models import Course, Topic, Register
from django.core.cache import cache


class HomeView(View):
    template_name = "index.html"

    def get(self, request):
        top_topic = cache.get_or_set("top_topics", Topic.objects.all())
        top_teacher = cache.get_or_set(
            "top_teachers", User.objects.filter(type="teacher")[:4]
        )
        top_course = cache.get_or_set(
            "top_courses", Course.objects.all().order_by("-register")[:4]
        )
        context = {
            "top_teacher": top_teacher,
            "top_course": top_course,
            "top_topic": top_topic,
        }
        return render(request, self.template_name, context)


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

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home")
        context = {"message": ""}
        return render(request, self.template_name, context)

    def post(self, request):
        form = SignUpForm(request.POST)
        error = " ".join([x for l in form.errors.values() for x in l])
        if not form.is_valid():
            context = {"message": error}
            return render(request, "registeration.html", context)
        form.create_user()
        if form.cleaned_data["type"] == "student":
            return redirect("login")
        else:
            return redirect("../admin")

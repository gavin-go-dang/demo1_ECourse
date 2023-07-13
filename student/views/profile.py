from django.shortcuts import render, redirect
from django.views.generic import View
from common.views import LoginRequired
from course_manager.models import Register, Certificate
from ..forms import UpdateUserInfoForm
from authen.models import User

# Create your views here.


class StudentProfile(LoginRequired, View):
    template_name = "student_info.html"

    def get(self, request):
        completed_course = Certificate.objects.filter(student=request.user)
        registered_course = Register.objects.filter(student=request.user).exclude(
            course__in=completed_course.values_list("course", flat=True)
        )
        context = {
            "user": request.user,
            "registered_course": registered_course,
            "completed_course": completed_course,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UpdateUserInfoForm(request.POST)
        if form.is_valid():
            user = request.user
            user.full_name = form.cleaned_data["full_name"]
            user.email = form.cleaned_data["email"]
            user.save()

        return redirect("/")

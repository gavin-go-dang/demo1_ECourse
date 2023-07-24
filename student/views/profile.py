from django.shortcuts import render, redirect
from django.views.generic import View
from common.views import LoginRequired
from course_manager.models import Register, Certificate
from ..forms import UpdateUserInfoForm, CoverImgForm
from authen.models import User

# Create your views here.


class StudentProfile(LoginRequired, View):
    template_name = "student_info.html"
    avt_form = CoverImgForm()

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
        if "update" in request.POST:
            form = UpdateUserInfoForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
            else:
                error = " ".join([x for l in form.errors.values() for x in l])
                context = {"message": error}
                return render(request, self.template_name, context)

        if "update_img" in request.POST:
            form = CoverImgForm(request.POST, request.FILES, instance=request.user)
            if form.is_valid():
                form.save()
        return redirect("./")

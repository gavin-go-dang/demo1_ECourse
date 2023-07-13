from django.shortcuts import render
from django.views.generic import View
from common.views import LoginRequired

# Create your views here.


class StudentProfile(LoginRequired, View):
    template_name = "student_info.html"

    def get(self, request, **kwargs):
        context = {"user": request.user}
        return render(request, self.template_name, context)

from django.shortcuts import redirect, render
from django.views.generic import ListView

from common.views import LoginRequired
from course_manager.models import Certificate, ResultTest


class ListResultExam(LoginRequired, ListView):
    template_name = "list_result.html"
    model = ResultTest

    def get_context_data(self, **kwargs):
        context = super(ListResultExam, self).get_context_data(**kwargs)
        context["object_list"] = ResultTest.objects.filter(student=self.request.user)
        return context

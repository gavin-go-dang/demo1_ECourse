from common.views import LoginRequired
from django.views.generic import TemplateView

# Create your views here.


class SummaryLearning(LoginRequired, TemplateView):
    template_name = "summary.html"

from django.urls import path, include
from .views import SummaryLearning


urlpatterns = [
    path("summary/", SummaryLearning.as_view(), name="summary"),
]

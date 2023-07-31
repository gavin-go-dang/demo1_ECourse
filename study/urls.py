from django.urls import include, path

from .views import (
    ExamContent,
    LessonContent,
    ListResultExam,
    ResultExam,
    CertificateContent,
    GeneratePdf,
)

urlpatterns = [
    path("lesson/<pk>/", LessonContent.as_view(), name="lesson"),
    path("exam/<pk>/", ExamContent.as_view(), name="exam"),
    path("result/<pk>/", ResultExam.as_view(), name="result"),
    path("result/", ListResultExam.as_view(), name="list_result"),
    path("result/<pk>/", ResultExam.as_view(), name="result"),
    path("cert/<int:student>/<int:course>/", CertificateContent.as_view(), name="cert"),
    path("cert_pdf/<int:student>/<int:course>/", GeneratePdf.as_view(), name="pdf"),
]

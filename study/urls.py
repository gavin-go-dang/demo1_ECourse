from django.urls import include, path

from .views import (
    CertificateContent,
    ExamContent,
    GenerateCertificatePdf,
    LessonContent,
    ListResultExam,
    ResultExam,
    CheckCertificate,
)

urlpatterns = [
    path("lesson/<pk>/", LessonContent.as_view(), name="lesson"),
    path("exam/<pk>/", ExamContent.as_view(), name="exam"),
    path("result/<pk>/", ResultExam.as_view(), name="result"),
    path("result/", ListResultExam.as_view(), name="list_result"),
    path("result/<pk>/", ResultExam.as_view(), name="result"),
    path("cert/<int:student>/<int:course>/", CertificateContent.as_view(), name="cert"),
    path("check/", CheckCertificate.as_view(), name="cert"),
    path(
        "cert_pdf/<int:student>/<int:course>/",
        GenerateCertificatePdf.as_view(),
        name="cert_pdf",
    ),
]

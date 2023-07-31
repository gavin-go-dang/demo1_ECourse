from django.views.generic import TemplateView
from django.shortcuts import render
from course_manager.models import Certificate


class CheckCertificate(TemplateView):
    template_name = "check_cert.html"

    def post(self, request):
        id_certificate = request.POST.get("id")
        try:
            cert = Certificate.objects.get(id=id_certificate)
            context = {"exist": True, "data": cert, "id": id_certificate}
            return render(request, self.template_name, context)
        except:
            return render(request, self.template_name, context={"exist": False})

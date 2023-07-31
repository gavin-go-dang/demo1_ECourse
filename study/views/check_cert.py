from django.views.generic import TemplateView
from django.shortcuts import render
from course_manager.models import Certificate
from django.db.models import Count, F, Value
import pickle
import zlib


def get_hash(obj):
    return zlib.adler32(pickle.dumps(obj))


def total_items(queryset):
    return queryset.count()


class CheckCertificate(TemplateView):
    template_name = "check_cert.html"

    def post(self, request):
        id_certificate = int(request.POST.get("id"))
        try:
            cert = Certificate.objects.all()
            list_hash = [get_hash(certificate) for certificate in cert]
            if id_certificate in list_hash:
                cert_valid = cert[list_hash.index(id_certificate)]
            breakpoint()
            context = {"exist": True, "data": cert_valid, "id": id_certificate}

            return render(request, self.template_name, context)
        except:
            return render(request, self.template_name, context={"exist": False})

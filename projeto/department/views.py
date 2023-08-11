from django.http import HttpResponse
from django.template.loader import get_template
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView

from . import serializers
from .models import Department
from pdfkit import from_string
class ListCreateDepartamentoView(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = serializers.DepartamentoSerializer

class DetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = serializers.DepartamentoSerializer

class DownloadUserRel(RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = serializers.DepartamentoSerializer

    def generate_pdf(self, users, department):

        data = {
            'users': users,
            'department': department
        }
        template = get_template('report.html')
        html = template.render(data)
        return from_string(html, False, options={
            'encoding': 'UTF-8',
            'page-size': 'A4',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            
        })

    def get(self, request, *args, **kwargs):
        department = self.get_object()
        users = department.users.all()
        filename = "relatorio_departamento.pdf"
        response = HttpResponse(self.generate_pdf(users=users, department=department), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="' + filename + '"'

        return response
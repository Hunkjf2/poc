from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from . import serializers
from .models import Department

class ListCreateDepartamentoView(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = serializers.DepartamentoCreateSerializer

class DetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = serializers.DepartamentoSerializer

from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from .models import Department

class CreateDepartamentoView(CreateAPIView):

    serializer_class = serializers.DepartamentoCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data

        return Response(data, status=status.HTTP_201_CREATED)
    
class ListarDepartamentoView(ListAPIView):

    serializer_class = serializers.DepartamentoSerializer

    def get(self, request):
        queryset = Department.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)
    
    
class ListarOneDepartamentoView(ListAPIView):

    serializer_class = serializers.DepartamentoSerializer

    def get(self, request, id):
        queryset = Department.objects.filter(pk=id)
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)
    
class EditDepartamentoView(UpdateAPIView):

    serializer_class = serializers.DepartamentoEditSerializer

    def put(self, request, id):

        descricao = request.data.get('descricao')
        queryset = Department.objects.filter(pk=id).update(descricao=descricao)
        self.get_serializer(queryset, many=True)

        getUsers = Department.objects.filter(pk=id)
        serializerTwo = self.get_serializer(getUsers, many=True)
        data = serializerTwo.data
        return Response(data, status=status.HTTP_200_OK)
    
    
class DeleteDepartamentoView(DestroyAPIView):

    serializer_class = serializers.DepartamentoDeleteSerializer

    def delete(self, request, id):
        queryset = Department.objects.filter(pk=id).delete()
        self.get_serializer(queryset, many=True)
        return Response({'ok'}, status=status.HTTP_200_OK)

# Create your views here.

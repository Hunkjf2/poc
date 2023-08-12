from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView, GenericAPIView

from rest_framework.response import Response
from rest_framework import status
from . import serializers
from .models import Users
from department.models import Department
import jwt
from django.conf import settings

#TODO: toda a parte de jwt foi feita para apenas playground, aconselho fazer via api's do DJANGO de JWT e também
#usar a estrutura de users do django, pois ja trabalha corretamente com crypto de senhas e sessão..
class LoginUser(GenericAPIView):
    serializer_class = serializers.UsersSerializer

    def post(self, request, *args, **kwargs):
        try:
            queryset = Users.objects.get(email=request.data['email'], password=request.data['password'])
            serializer = self.get_serializer(queryset)
            data = serializer.data

            encoded_data = jwt.encode(data,
                              key=settings.SECRET_KEY,
                              algorithm="HS256")


            data["tokens"] = str(encoded_data)

            return Response(data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response("Incorrect email or password", status=status.HTTP_400_BAD_REQUEST)


class CreateUsersView(CreateAPIView):

    serializer_class = serializers.UsersCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data

        return Response(data, status=status.HTTP_201_CREATED)
    
    
class ListarUsersView(ListAPIView):

    serializer_class = serializers.UsersSerializer

    def get(self, request):
        queryset = Users.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)
    

class ListarOneUsersView(RetrieveAPIView):
    queryset = Users.objects.all()
    serializer_class = serializers.UsersSerializer

    
class EditUsersView(UpdateAPIView):

    serializer_class = serializers.UsersEditSerializer

    def put(self, request, id):

        nome = request.data.get('nome')
        cpf = request.data.get('cpf')
        email = request.data.get('email')
        cargo = request.data.get('cargo')
        departamentoId = request.data.get('departamentoId')
        queryset = Users.objects.filter(pk=id).update(nome=nome,cpf=cpf,email=email,cargo=cargo,departamentoId=departamentoId)
        self.get_serializer(queryset, many=True)

        getUsers = Users.objects.filter(pk=id)
        serializerTwo = self.get_serializer(getUsers, many=True)
        data = serializerTwo.data
        return Response(data, status=status.HTTP_200_OK)
    
    
class DeleteUsersView(DestroyAPIView):

    serializer_class = serializers.UsersDeleteSerializer

    def delete(self, request, id):
        queryset = Users.objects.filter(pk=id).delete()
        self.get_serializer(queryset, many=True)
        return Response({'ok'}, status=status.HTTP_200_OK)
    

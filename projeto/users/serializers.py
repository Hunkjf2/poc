from rest_framework import serializers
from .models import Users, Department

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'descricao']


class UsersSerializer(serializers.ModelSerializer):
    departments = DepartamentoSerializer(many=True, read_only=True)

    class Meta:
        model=Users
        fields= ['id','nome','cpf','email','cargo','departamentoId','departments']

class UsersCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields= ("nome","cpf","email","cargo","departamentoId",)

class UsersEditSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields= ("nome","cpf","email","cargo","departamentoId",)

class UsersDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields= ("id",)
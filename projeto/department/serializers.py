from rest_framework import serializers
from .models import Department

class DepartamentoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields= ("descricao",)

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields= "__all__"

class DepartamentoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields= ("descricao",)

class DepartamentoEditSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields= ("descricao",)

class DepartamentoDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields= ("id",)

class UsersByDepartamentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields= ("id","descricao","users")
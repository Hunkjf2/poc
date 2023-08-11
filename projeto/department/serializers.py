from rest_framework import serializers
from .models import Department
class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields= ['id', 'descricao']
        
class UsersByDepartamentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields= ("id","descricao","users")
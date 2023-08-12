from django.db import models
from department.models import Department

class Users(models.Model):
    nome = models.CharField(max_length=250)
    password = models.CharField(max_length=50, default="password")
    cpf = models.CharField(max_length=20)
    email = models.CharField(max_length=250)
    cargo = models.CharField(max_length=250)
    departamentoId = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='users')
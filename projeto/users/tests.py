from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Users,Department
from . import serializers
from rest_framework import serializers
class UserApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_object(self):
        self.departament = Department.objects.create(
          descricao='test category',
        )
        data = {'nome': 'asas','cpf':'2121212','email':'teste@hotmail.com','cargo':'teste','departamentoId':self.departament.id}
        response2 = self.client.post('/users/criar', data, format='json')
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)

    def test_list_object(self):
        response = self.client.get('/users', follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_object(self):
        response = self.client.delete('/users/delete/23')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_object(self):
        self.departament = Department.objects.create(
          descricao='test category',
        )
        data = {'nome': 'asas','cpf':'2121212','email':'teste@hotmail.com','cargo':'teste','departamentoId':self.departament.id}
        response = self.client.put('/users/editar/23', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
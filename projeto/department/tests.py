from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Department
from . import serializers
from rest_framework import serializers
class DepartamentApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_object(self):
        data = {'descricao': 'asas'}
        response = self.client.post('/department/criar', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_object(self):
        response = self.client.get('/department', follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_object(self):
        response = self.client.delete('/department/delete/23')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_object(self):
        data = {'descricao': '1122'}
        response = self.client.put('/department/editar/23', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
# from django.test import TestCase
from rest_framework import test
from rest_framework import status
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from django.urls import reverse

class RegisterTestCase(test.APITestCase):
    
    def test_register(self):
        data = {
            "username": "testcase",
            "email": "test1@example.com",
            "password": "test@123",
            "password2": "test@123",
        }
        response = self.client.post(reverse('register-page'),data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
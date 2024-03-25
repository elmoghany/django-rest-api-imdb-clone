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
        
class LoginLogoutTestCase(test.APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="test@123")
        
    def test_login(self):
        data = {
            "username": "example",
            "password": "test@123"
        }
        response = self.client.post(reverse('login-page'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_logout(self):
        self.token = Token.objects.get(username__username="example")
        self.client.credentials(HTTP_AUTHORIZATION="Token" + self.token.key)
        response = self.client.post(reverse('logout-page'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

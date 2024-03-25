# from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import test
from rest_framework import status
from rest_framework.authtoken.models import Token
from watchlist_app.api import serializers
from watchlist_app.api import models

class StreamPlatformTestCase(test.APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="test@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
    
    def test_streamplatform_create(self):
        data = {
            "name": "netflix",
            "about": "#1 streaming platform",
            "website": "https://netflix.com"
        }
        response = self.client.post(reverse('streamplatform-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
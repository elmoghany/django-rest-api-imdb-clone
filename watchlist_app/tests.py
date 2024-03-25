# from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import test
from rest_framework import status
from rest_framework.authtoken.models import Token
from watchlist_app.api import serializers
from watchlist_app import models

class StreamPlatformTestCase(test.APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="test@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        self.stream = models.StreamPlatform.objects.create(name="netflix", about="# sds sd", website="https://wnndnd.com")
    
    def test_streamplatform_create(self):
        data = {
            "name": "netflix",
            "about": "#1 streaming platform",
            "website": "https://netflix.com"
        }
        response = self.client.post(reverse('streamplatform-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_streamplatform_list(self):
        response = self.client.get(reverse('streamplatform-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_streamplatform_individual(self):
        response = self.client.get(reverse('streamplatform-detail', args=(self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class WatchListTestCase(test.APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="test@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        self.stream = models.StreamPlatform.objects.create(name="netflix", about="# sds sd", website="https://wnndnd.com")
        self.watchlist = models.WatchList.objects.create(platform=self.stream, title="example movie", description="description storyline", active=True)
    
    def test_watchlist_create(self):
        data = {
            "platform" : self.stream,
            "title": "example movie",
            "storyline": "example story",
            "active": True
        }
        response = self.client.post(reverse('watch-list-page'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_watchlist_list(self):
        response = self.client.get(reverse('watch-list-page'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_watchlist_individual(self):
        response = self.client.get(reverse('watch-detail-page', args=self.watchlist.id,))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

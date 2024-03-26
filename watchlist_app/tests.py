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
            "description": "example story",
            "active": True
        }
        response = self.client.post(reverse('watch-list-page'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_watchlist_list(self):
        response = self.client.get(reverse('watch-list-page'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_watchlist_individual(self):
        response = self.client.get(reverse('watch-detail-page', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.WatchList.objects.get().title, "example movie")
        self.assertEqual(models.WatchList.objects.count(), 1)
        
        
class ReviewTestCase(test.APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="test@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = models.StreamPlatform.objects.create(name="netflix", 
                                                           about="# sds sd", 
                                                           website="https://www.wnndnd.com")
        self.watchlist = models.WatchList.objects.create(platform=self.stream, 
                                                         title="example movie", 
                                                         description="description storyline", 
                                                         active=True)
        self.watchlist2 = models.WatchList.objects.create(platform=self.stream, 
                                                         title="example movie", 
                                                         description="description storyline", 
                                                         active=True)
        self.review = models.Review.objects.create(review_username=self.user, rating=5, description="bla bla", watchlist=self.watchlist2, active=True)
        
    def test_review_create(self):
        data = {
            "review_username" : self.user,
            "rating": 5,
            "description": "great movie",
            "watchlist": self.watchlist,
            "active": True
        }
        response = self.client.post(reverse('review-create-page', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(reverse('review-create-page', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_review_create_unauth(self):
        data = {
            "review_username" : self.user,
            "rating": 5,
            "description": "great movie",
            "watchlist": self.watchlist,
            "active": True
        }
        self.client.force_authenticate(user=None)
        response = self.client.post(reverse('review-create-page', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_review_update(self):
        data = {
            "review_username" : self.user,
            "rating": 4,
            "description": "great movie - updated",
            "watchlist": self.watchlist,
            "active": False
        }
        response = self.client.put(reverse('review-detail-page', args=(self.review.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_list(self):
        response = self.client.get(reverse('review-list-page', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_review_individual(self):
        response = self.client.get(reverse('review-detail-page', args=(self.review.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_review_user(self):
        response = self.client.get('/watch/reviews/?username' + self.user.username)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
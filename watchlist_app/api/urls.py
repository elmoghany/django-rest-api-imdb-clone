from django.urls import path
from watchlist_app.api.views import movie_list, movie_detail

urlpatterns = [
    path('list/', movie_list, name='movie-list-page'),
    path('<int:pk>/', movie_detail, name='movie-detail-page'),
]

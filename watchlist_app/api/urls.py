from django.urls import path
# from watchlist_app.api.views import movie_list, movie_detail

# urlpatterns = [
#     path('list/', movie_list, name='movie-list-page'),
#     path('<int:pk>/', movie_detail, name='movie-detail-page'),
# ]

from watchlist_app.api.views import MovieDetailAV, MovieListAV
urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie-list-page'),
    path('<int:pk>/', MovieDetailAV.as_view(), name='movie-detail-page'),
]

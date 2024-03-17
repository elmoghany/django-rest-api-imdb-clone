from django.urls import path
# from watchlist_app.api.views import movie_list, movie_detail

# urlpatterns = [
#     path('list/', movie_list, name='movie-list-page'),
#     path('<int:pk>/', movie_detail, name='movie-detail-page'),
# ]

from watchlist_app.api.views import WatchDetailAV, WatchListAV, StreamPlatformAV, StreamDetailAV
urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch-list-page'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='watch-detail-page'),
    path('stream/', StreamPlatformAV.as_view(), name='streamplatform-page'),
    path('stream/<int:pk>/', StreamDetailAV.as_view(), name='streamplatform-detail'),
]

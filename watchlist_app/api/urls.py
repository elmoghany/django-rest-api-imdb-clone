from rest_framework.routers import DefaultRouter
from django.urls import include, path
# from watchlist_app.api.views import movie_list, movie_detail

# urlpatterns = [
#     path('list/', movie_list, name='movie-list-page'),
#     path('<int:pk>/', movie_detail, name='movie-detail-page'),
# ]

from watchlist_app.api.views import (WatchDetailAV, WatchListAV, 
                                    StreamPlatformAV, StreamDetailAV, StreamPlatformVS,
                                    ReviewList, ReviewDetail, ReviewCreate,
                                    UserReview)

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename="streamplatform")

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch-list-page'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='watch-detail-page'),
    path('', include(router.urls)),
    # path('stream/', StreamPlatformAV.as_view(), name='streamplatform-page'),
    # path('stream/<int:pk>/', StreamDetailAV.as_view(), name='streamplatform-detail'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail-page'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-page'),
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create-page'),
    
    #search using a link
    # path('reviews/<str:username>', UserReview.as_view(), name='user-review-detail-page'),
    #search using parameters
    path('reviews/', UserReview.as_view(), name='user-review-detail-page'),
]

from rest_framework import routers
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from .views import (UserProfileAPIView, CountryAPIView, CountryDetailAPIView, DirectorAPIView, DirectorDetailAPIView, ActorAPIView, ActorDetailAPIView, GenreAPIView, MovieAPIView, MovieDetailAPIView, MovieLanguagesAPIView, MovieMomentsAPIView, RatingAPIView, SaveToFavoriteAPIView, FavoriteMoviesAPIView, HistoryAPIView, RegisterView, CustomLoginView, LogoutView)


# router = routers.SimpleRouter()


urlpatterns = [
    # path('', include(router.urls)),
    path('', MovieAPIView.as_view(), name = 'movies'),
    path('movie/<int:pk>/', MovieDetailAPIView.as_view(), name = 'movie_details'),
    path('genre/', GenreAPIView.as_view(), name = 'genrs'),
    path('genre/<int:pk>/', GenreAPIView.as_view(), name = 'genrs-details'),
    path('country/', CountryAPIView.as_view(), name = 'countries'),
    path('country/<int:pk>', CountryDetailAPIView.as_view(), name = 'countries-details'),
    path('director/', DirectorAPIView.as_view(), name = 'directors'),
    path('director/<int:pk>', DirectorDetailAPIView.as_view(), name = 'directors-details'),
    path('actor/', ActorAPIView.as_view(), name = 'actors'),
    path('actor/<int:pk>', ActorDetailAPIView.as_view(), name = 'actors-details'),

    path('history/', HistoryAPIView.as_view(), name = 'histories'),
    path('favorite_movie/', FavoriteMoviesAPIView.as_view(), name = 'favorite_movies'),
    path('user/', UserProfileAPIView.as_view(), name = 'user'),
    path('register/', RegisterView.as_view(), name = 'register'),
    path('login/', CustomLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui')
]

from rest_framework import routers
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from .views import (UserProfileViewSet, CountryAPIView, DirectorAPIView, ActorAPIView, GenreAPIView, MovieAPIView, MovieDetailAPIView, MovieLanguagesViewSet, MovieMomentsViewSet, RatingViewSet, SaveToFavoriteViewSet, FavoriteMoviesViewSet, HistoryViewSet, RegisterView, CustomLoginView, LogoutView)


router = routers.SimpleRouter()
router.register(r'user', UserProfileViewSet, basename = 'users')
router.register(r'movie_language', MovieLanguagesViewSet, basename = 'movie_languages')
router.register(r'movie_moment', MovieMomentsViewSet, basename = 'movie_moments')
router.register(r'rating', RatingViewSet, basename = 'ratings')
router.register(r'save_to_favorite', SaveToFavoriteViewSet, basename = 'save_to_favorites')
router.register(r'favorite_movie', FavoriteMoviesViewSet, basename = 'favorite_movies')
router.register(r'history', HistoryViewSet, basename = 'histories')


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name = 'register'),
    path('login/', CustomLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    path('movie/', MovieAPIView.as_view(), name = 'movies'),
    path('movie/<int:pk>/', MovieDetailAPIView.as_view(), name = 'movie_details'),
    path('genre/', GenreAPIView.as_view(), name = 'genrs'),
    path('country/', CountryAPIView.as_view(), name = 'countries'),
    path('director/', DirectorAPIView.as_view(), name = 'directors'),
    path('actor/', ActorAPIView.as_view(), name = 'actors'),
]

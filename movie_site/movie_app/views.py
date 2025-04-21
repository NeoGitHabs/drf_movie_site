from  rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, generics, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import UserProfile, Country, Director, Actor, Genre, Movie, MovieLanguages, MovieMoments, Rating, SaveToFavorite, FavoriteMovies, History
from .filters import MovieFilter
from .serializers import (UserProfileSerializers, CountrySerializers, DirectorSerializers, ActorSerializers,
                          GenreSerializers, MovieSerializers, MovieDetailSerializers, MovieLanguagesSerializers, MovieMomentsSerializers,
                          RatingSerializers, SaveToFavoriteSerializers, FavoriteMoviesSerializers, HistorySerializers,
                          LoginSerializer, UserSerializer)


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)

class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

# --------------------------------------------------------------------------------------
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers

class CountryAPIView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializers

class DirectorAPIView(generics.ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializers

class ActorAPIView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializers

class GenreAPIView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers

class MovieAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers

    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_class = MovieFilter
    ordering_fields = ['year']
    search_fields = ['movie_name']

class MovieDetailAPIView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializers

    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_class = MovieFilter
    ordering_fields = ['year']
    search_fields = ['movie_name']

class MovieLanguagesViewSet(viewsets.ModelViewSet):
    queryset = MovieLanguages.objects.all()
    serializer_class = MovieLanguagesSerializers

class MovieMomentsViewSet(viewsets.ModelViewSet):
    queryset = MovieMoments.objects.all()
    serializer_class = MovieMomentsSerializers

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers

class SaveToFavoriteViewSet(viewsets.ModelViewSet):
    queryset = SaveToFavorite.objects.all()
    serializer_class = SaveToFavoriteSerializers

class FavoriteMoviesViewSet(viewsets.ModelViewSet):
    queryset = FavoriteMovies.objects.all()
    serializer_class = FavoriteMoviesSerializers

class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializers

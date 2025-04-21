from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField

STATUS_CHOICES = (
    ('simple', 'simple'),
    ('pro', 'pro'),
)

class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(15), MaxValueValidator(65)], null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='simple')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

class Country(models.Model):
   country_name = models.CharField(max_length=32, unique=True)

   def __str__(self):
       return self.country_name

class Director(models.Model):
    director_name = models.CharField(max_length=100)
    bio = models.TextField()
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(15), MaxValueValidator(100)])
    director_image = models.ImageField(upload_to='director_images/')

    def __str__(self):
        return self.director_name

class Actor(models.Model):
    actor_name = models.CharField(max_length=100)
    bio = models.TextField()
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(15), MaxValueValidator(100)])
    actor_image = models.ImageField(upload_to='actor_images/')

    def __str__(self):
        return self.actor_name

class Genre(models.Model):
    genre_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.genre_name

class Movie(models.Model):
    movie_name = models.CharField(max_length=64)
    year = models.DateField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    director = models.ManyToManyField(Director)
    actor = models.ManyToManyField(Actor)
    genre = models.ManyToManyField(Genre)
    QUALITY_CHOICES = (
        ('144p', '144p'),
        ('360p', '360p'),
        ('480p', '480p'),
        ('720p', '720p'),
        ('1080p', '1080p')
    )
    quality = MultiSelectField(max_length=32,choices=QUALITY_CHOICES, max_choices=5) # type
    movie_time = models.PositiveSmallIntegerField()
    description = models.TextField()
    movie_trailer = models.URLField()
    movie_image = models.ImageField(upload_to='movie_poster/')
    status_movie = models.CharField(max_length=12, choices=STATUS_CHOICES)

    def __str__(self):
        return self.movie_name

    def avg_rating(self):
        rating = self.rating_connect_movie.all()
        if rating.exists():
            return round(sum([i.stars for i in rating]) / rating.count(), 1)
        return 0

    def count_user(self):
        return self.rating_connect_movie.count()

class MovieLanguages(models.Model):
    movie_dubbing = models.CharField(max_length=32, unique=True) # озвучкасы movie_videos
    video = models.FileField(upload_to='movie_videos/')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_videos_connect_movie')

    def __str__(self):
        return f'{self.movie}, {self.movie_dubbing}'

class MovieMoments(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_moments_connect_movie')
    movie_moments = models.ImageField(upload_to='movie_moments/')

    def __str__(self):
        return f'{self.movie}'

class Rating(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='rating_connect_movie')
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 11)])
    text = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}, {self.movie}'

class SaveToFavorite(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'

class FavoriteMovies(models.Model):
    save_to_favorite = models.ForeignKey(SaveToFavorite, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

class History(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)

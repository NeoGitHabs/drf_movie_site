from modeltranslation.translator import TranslationOptions, register
from .models import Movie, Country, Director, Actor, Genre, MovieLanguages, Rating


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name',)

@register(Director)
class DirectorTranslationOptions(TranslationOptions):
    fields = ('director_name', 'bio')

@register(Actor)
class ActorTranslationOptions(TranslationOptions):
    fields = ('actor_name', 'bio')

@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ('genre_name',)

@register(Movie)
class MovieTranslationOptions(TranslationOptions):
    fields = ('movie_name', 'description')

@register(MovieLanguages)
class MovieLanguagesTranslationOptions(TranslationOptions):
    fields = ('movie_dubbing',)

@register(Rating)
class RatingTranslationOptions(TranslationOptions):
    fields = ('text',)

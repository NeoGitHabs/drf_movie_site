from django.contrib import admin
from .models import UserProfile, Country, Director, Actor, Genre, Movie, MovieLanguages, MovieMoments, Rating, SaveToFavorite, FavoriteMovies, History
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin


class MovieLanguagesInlines(admin.TabularInline, TranslationInlineModelAdmin):
    model = MovieLanguages
    extra = 1

class MovieMomentsInlines(admin.TabularInline):
    model = MovieMoments
    extra = 1

@admin.register(Movie)
class MovieAdmin(TranslationAdmin):
    inlines = [MovieMomentsInlines, MovieLanguagesInlines]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Country, Director, Actor, Genre, MovieLanguages, Rating)
class TranslateAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(UserProfile)
admin.site.register(MovieMoments)
admin.site.register(SaveToFavorite)
admin.site.register(FavoriteMovies)
admin.site.register(History)


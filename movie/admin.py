from django.contrib import admin

# Register your models here.
from movie.models import Genre, Person, Movie, WatchList


class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class PersonAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "release_date", "genre")
    list_filter = ("genres__name",)
    search_fields = ("title", "director__name")


class WatchListAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "user")


admin.site.register(Genre, GenreAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(WatchList)
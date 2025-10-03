from django.contrib import admin
from .models import Movie, Review, HiddenMovie

class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']

class HiddenMovieAdmin(admin.ModelAdmin):
    list_display = ['user', 'movie', 'hidden_at', 'id']
    list_filter = ['hidden_at']

admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)
admin.site.register(HiddenMovie)
from django.contrib import admin
from .models import Petition, Vote


@admin.register(Petition)
class PetitionAdmin(admin.ModelAdmin):
	list_display = ("movie_name", "reason", "created_at")
	search_fields = ("movie_name", "reason")
	readonly_fields = ("created_at",)


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
	list_display = ("petition", "user", "is_upvote", "created_at")
	search_fields = ("petition__movie_name", "user__username")
	readonly_fields = ("created_at",)

from django.db import models
from django.conf import settings


class Petition(models.Model):
	"""A petition to request a movie be added or made visible.

	Fields:
	- movie_name: short name/title of the movie being requested
	- movie_description: short description of the movie (optional)
	- reason: why the petition is being made (required)
	- created_at: timestamp when the petition was created
	"""

	movie_name = models.CharField(max_length=200, verbose_name="Movie name")
	movie_description = models.TextField(
		blank=True, verbose_name="Movie description"
	)
	reason = models.TextField(verbose_name="Reason for petition")
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["-created_at"]
		verbose_name = "Petition"
		verbose_name_plural = "Petitions"

	def __str__(self) -> str:
		return f"Petition: {self.movie_name}"


class Vote(models.Model):
	"""A user's vote on a petition. One vote per user per petition.

	is_upvote=True means an affirmative vote; False indicates a negative vote.
	"""

	petition = models.ForeignKey(
		Petition, related_name="votes", on_delete=models.CASCADE
	)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	is_upvote = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		unique_together = ("petition", "user")
		ordering = ["-created_at"]

	def __str__(self) -> str:
		return f"Vote(user={self.user}, petition={self.petition_id}, up={self.is_upvote})"


def petition_yes_count(self):
	return self.votes.filter(is_upvote=True).count()


def petition_no_count(self):
	return self.votes.filter(is_upvote=False).count()


def petition_user_vote(self, user):
	if not user or not user.is_authenticated:
		return None
	try:
		return self.votes.get(user=user)
	except Vote.DoesNotExist:
		return None


# attach helper methods to Petition
Petition.yes_count = petition_yes_count
Petition.no_count = petition_no_count
Petition.user_vote = petition_user_vote

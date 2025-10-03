from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Petition
from .forms import PetitionForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Vote


def petition_list(request):
	"""Show a list of petitions."""
	petitions = Petition.objects.all()

	# attach user's vote object to each petition for easy template access
	user_votes = {}
	if request.user.is_authenticated:
		votes = Vote.objects.filter(user=request.user, petition__in=petitions)
		user_votes = {v.petition_id: v for v in votes}
	for p in petitions:
		# attach as 'user_vote' (no leading underscore) so the template can access it
		p.user_vote = user_votes.get(p.id)

	return render(request, "petition/list.html", {"petitions": petitions, "template_data": {"title": "Petitions"}})


def petition_create(request):
	"""Create a new petition. On success redirect to the petition list."""
	if request.method == "POST":
		form = PetitionForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(reverse("petition:list"))
	else:
		form = PetitionForm()

	return render(request, "petition/create.html", {"form": form, "template_data": {"title": "Create Petition"}})


@login_required
def petition_vote(request, petition_id):
	"""Handle voting (yes/no) on a petition. Expects POST with 'vote'='yes'|'no'."""
	if request.method != "POST":
		return HttpResponseForbidden("POST required")

	petition = Petition.objects.filter(id=petition_id).first()
	if not petition:
		return HttpResponseForbidden("Invalid petition")

	vote_val = request.POST.get("vote")
	if vote_val not in ("yes", "no"):
		return HttpResponseForbidden("Invalid vote value")
	is_up = vote_val == "yes"

	# either create or update the user's vote
	vote, created = Vote.objects.update_or_create(
		petition=petition, user=request.user, defaults={"is_upvote": is_up},
	)
	# redirect back to list
	return redirect(reverse("petition:list"))

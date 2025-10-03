from django import forms
from .models import Petition


class PetitionForm(forms.ModelForm):
    class Meta:
        model = Petition
        fields = ["movie_name", "movie_description", "reason"]
        widgets = {
            "movie_name": forms.TextInput(attrs={"class": "form-control"}),
            "movie_description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "reason": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }

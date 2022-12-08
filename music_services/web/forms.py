from django import forms
from music_services.web.models import Recommendation


class RecommendationCreateForm(forms.ModelForm):
    class Meta:
        model = Recommendation
        fields = '__all__'


from django import forms
from .models import Project

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'image', 'title', 'link', 'description', 'date_added'
        ]







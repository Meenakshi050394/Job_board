from django import forms
from .models import JobPost, Review, Application

class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = ['title', 'description', 'company']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = []

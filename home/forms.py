from django import forms
from home.models import Summary

class SummaryForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
    }))
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
    }))
    surname = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
    }))
    number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
    }))
    education = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control py-4',
    }))
    experience = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control py-4',
    }))
    skills = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control py-4',
    }))
    languages = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control py-4',
    }))

    class Meta:
        model = Summary
        fields = ('name', 'surname', 'email', 'number', 'education', 'experience', 'skills', 'languages')

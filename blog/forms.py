from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'col-sm-12'
            }),
            'email': forms.TextInput(attrs={
                'class': 'col-sm-12'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control'
            })
        }
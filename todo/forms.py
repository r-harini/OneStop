from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):

    title=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add a new task...'}))

    class Meta:
        model = Task #which model are we creating for the form for
        fields='__all__' # what fields are we going to allow in the form
    
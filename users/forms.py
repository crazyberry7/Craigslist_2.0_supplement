from django import forms
from django.contrib.auth.forms import UserCreationForm


from .models import customuser



class CustomUserCreationForm(forms.ModelForm):

    class Meta:
        model = customuser
        fields = ('username', 'email')

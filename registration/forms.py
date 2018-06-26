from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.', widget=forms.TextInput(attrs={'placeholder':'Email'}))
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder':'Username'})) 
    password1 = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder':'Enter password again'}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2', )

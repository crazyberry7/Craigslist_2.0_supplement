from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import auth
#from django.contrib.auth.forms import UserCreationForm

from registration.forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('http://127.0.0.1:8000/search')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('http://127.0.0.1:8000/users/login')

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import customuser
from .forms import CustomUserCreationForm
import json
import sys
#from oauth2client import client
#from flask import make_response, session, request, render_template, Flask
# Create your views here.




@login_required
def my_profile(request):
   
    """
    user_instance = get_object_or_404(customuser, id=id)

    context = {
	'first_name': user_instance.first_name,
	'last_name': user_instance.last_name,
	'email': user_instance.email,
	'username': user_instance.username,
	'instance': user_instance,
    }
    """
    if request.GET.get('q') or request.GET.get('zipcode'):
        query = request.GET.get('q') 
        zipcode = request.GET.get('zipcode')
        url = '/search/?q='+ query+'&zipcode=' + zipcode
        return HttpResponseRedirect(url)

    else:
        #import pdb; pdb.set_trace()
        if request.method == "POST":
            form = CustomUserCreationForm(data=request.POST, instance=request.user)
            if form.is_valid():
                user = form.save(commit=False)
                user.save()

    return render(request, 'my_profile.html') 




















"""
def login(request):



def logout(request):
	logout(request)

if os.path.isfile('client_secrets.json') is False:
    sys.exit('client_secrets.json not found')
CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']

def login(request):
    id_token = request.form.get('id_token', '')
    
    idinfo = client.verify_id_token(id_token, CLIENT_ID)
    if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
        return make_response('Wrong Issuer.', 401)

    sub = idinfo['sub']

    store = CredentialStore.get_by_id(sub)

    if store is None:
        store = CredentialStore(id=sub, id_token=idinfo)
    else:
        store.id_token = idinfo

    store.put()
    session['id'] = sub
    return render(request, 'login.html')
"""    

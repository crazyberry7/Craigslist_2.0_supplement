from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
import json
import sys
from oauth2client import client
from flask import make_response, session, request, render_template, Flask
# Create your views here.


"""
def login(request):



def logout(request):
	logout(request)

"""
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
    

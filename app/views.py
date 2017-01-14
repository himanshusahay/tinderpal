from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
import pynder
import pynder.api as api
import requests
import json

def index(request):
	return render(request, 'app/index.html')

def login(request):
	request.session['facebook_id'] = request.POST['facebook_id']
	request.session['facebook_auth_token'] = request.POST['facebook_access_token']
	return HttpResponse("Success")

def landing(request):
	facebook_id = request.session['facebook_id']
	facebook_auth_token = request.session['facebook_auth_token']
	# session = pynder.Session(facebook_id, facebook_auth_token)
	# num_matches = len(session.matches())
	# ap = api.Ti?nderAPI()
	# print("API", ap.auth(facebook_id, facebook_auth_token))
	# r = requests.post("http://api.gotinder.com/auth", headers={'app-version': '3', 'platform': 'ios'}, data=json.dumps({'facebook_id': str(facebook_id), 'facebook_token': facebook_auth_token}))
	# print("R:", r.json())

	return render(request, 'app/landing.html', {"id": facebook_id, "token": facebook_auth_token})

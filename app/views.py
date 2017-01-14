from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse

def index(request):
	return render(request, 'app/index.html')

def login(request):
	return HttpResponse("Success")

def landing(request):
	return render(request, 'app/landing.html')

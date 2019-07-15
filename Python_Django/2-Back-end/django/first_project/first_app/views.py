from django.shortcuts import render
from django.http import HttpResponse # Add this

# Create your views here.

# Each view exist as a function, and takes atleast one argument usually 'request' and each must return an httpResponse object which takes a string arg of what to render on the view.
# Each view must be mapped to a url in urls.py

def index(request):
	return HttpResponse('Hello world')



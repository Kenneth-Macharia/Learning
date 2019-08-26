from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse('Welcome to AppTwo')

def test(request):
	render_dict = {'insert_me':'Test Page'}
	return render(request, 'AppTwo/test.html', context=render_dict)
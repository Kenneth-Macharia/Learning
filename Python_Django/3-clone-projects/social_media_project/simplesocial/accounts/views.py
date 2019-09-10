from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from . import forms

class SignUp(CreateView):
	''' New user view '''
	
	form_class = forms.UserCreateForm
	success_url = reverse_lazy('login')  # After registration, redirect to login page
	template_name = 'accounts/signup.html'



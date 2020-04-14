from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
	return render(request, 'forms_app/index.html')

def form_view(request):
	form = forms.FormName()

	if request.method == 'POST':
		form = forms.FormName(request.POST)

		if form.is_valid():  # Forms get a cleaned_data attr after is_valid() has passed
			print('Name:', form.cleaned_data['name'])
			print('Email:', form.cleaned_data['email'])
			print('Text:', form.cleaned_data['text'])

	return render(request, 'forms_app/form.html', {'form': form})

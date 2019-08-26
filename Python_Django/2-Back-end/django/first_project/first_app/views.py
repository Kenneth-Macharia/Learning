from django.shortcuts import render  # Use this for inserting dyamic content into html file
# from django.http import HttpResponse # Use this for displaying static text

from first_app.models import AccessRecord, Webpage, Topic  # Import required models

# Create your views here.

# Each view exist as a function, and takes atleast one argument usually 'request' and each must return an httpResponse object which takes a string arg of what to render on the view.
# Each view must be mapped to a url in urls.py

def index(request):

	# Query model for database data and sort them by date accessed. Note the are related.
	webpage_list = AccessRecord.objects.order_by('page_accessed_date')

	pages_dict = {'page_records': webpage_list}
	return render(request, 'first_app/index.html', context=pages_dict)



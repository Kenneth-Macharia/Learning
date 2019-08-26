# from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (View, TemplateView, ListView, DetailView, CreateView, UpdateView, 							DeleteView)
from . import models


# class CBV_view(View):

# 	def get(self, request):
# 		return HttpResponse('CLASS BASED VIEW SHOWING!')


class IndexView(TemplateView):
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['added_data'] = 'I WAS INJECTED INTO INDEX.HTML!'
		return context


# CBVs with models
class SchoolListView(ListView):  # Schools list only

	# The ListView class will create a list from the model name, lower case it and add _list to it.
	# However, this defautl behaviour can be overriden by declaring a class context attribute, set to the required list name for better clarity, eg. context_object_name = 'schools'

	model = models.School


class SchoolDetailView(DetailView):  # School details

	# The DetailView class returns the list with the model name, lower case only.

	context_object_name = 'school_detail'
	model = models.School
	template_name = 'cbvs_app/school_detail.html'


class SchoolCreateView(CreateView):
	# Define the view fields corresposnding to the model
	fields = ('name', 'principal', 'location')
	model = models.School


class SchoolUpdateView(UpdateView):
	fields = ('name', 'principal')
	model = models.School


class SchoolDeleteView(DeleteView):
	model = models.School

	# Success attribute
	success_url = reverse_lazy('cbvs_app:list') 







from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import (LoginRequiredMixin, PermissionRequiredMixin)
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Group, GroupMember
from . import models
from django.contrib import messages
from django.db import IntegrityError


class CreateGroup(LoginRequiredMixin, generic.CreateView):
	''' Render the group creation page '''

	fields = ('name', 'description')
	model = Group


class SingleGroup(generic.DetailView):
	''' Render the group details page '''
	
	model = Group


class ListGroups(generic.ListView):
	''' Render group list '''

	model = Group


class JoinGroup(LoginRequiredMixin, generic.RedirectView):
	''' Group joining redirect view '''

	def get_redirect_url(self, *args, **kwargs):
		''' Once joined a group redirect to the group's posts detail page '''

		return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

	def get(self, request, *args, **kwargs):
		''' Check that a user is not a group member before joining a group '''

		group = get_object_or_404(Group, slug=self.kwargs.get('slug'))

		try:
			GroupMember.objects.create(user=self.request.user, group=group)

		except IntegrityError:
			messages.warning(self.request, 'Already a member!')

		else:
			messages.success(self.request, 'You are now a member!')

		return super().get(request, *args, **kwargs)


class LeaveGroup(LoginRequiredMixin, generic.RedirectView):
	''' Group leave redirect view '''

	def get_redirect_url(self, *args, **kwargs):
		''' Once having left a group redirect to the group's posts detail page '''

		return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

	def get(self, request, *args, **kwargs):
		''' Check that a user is not a group member before trying to leave the group '''

		try:
			membership = models.GroupMember.objects.filter(user=self.request.user,
														 group__slug=self.kwargs.get('slug')).get()

		except models.GroupMember.DoesNotExist:
			messages.warning(self.request, 'Sorry, you are not a member of this group!')

		else:
			membership.delete()
			messages.success(self.request, 'You have successfully left the group!')

		return super().get(request, *args, **kwargs)
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.views import generic
from django.contrib import messages
from braces.views import SelectRelatedMixin  # Adds more auth mixins
from . import models
from . import forms

from django.contrib.auth import get_user_model  # Fetches the currently logged in user
User = get_user_model()


class PostList(SelectRelatedMixin, generic.ListView):
	''' Displays the list of posts related to a group or a user, by selecting either a group or a user or both '''

	model = models.Post
	select_related = ('user', 'group')  # Foreignkeys for post related model i.e user & group


class UserPosts(generic.ListView):
	''' Generic view for a specific user's posts '''

	model = models.Post
	template_name = 'posts/user_post_list.html'

	def get_queryset(self):
		''' Fetches a users posts '''

		try:
			self.post_user = User.objects.prefetch_related('posts').get(
																		username__iexact=self.
																		kwargs.get('username'))
		except User.DoesNotExist:
			raise Http404

		else:
			return self.post_user.posts.all()

	def get_context_data(self, **kwargs):
		
	    context = super().get_context_data(**kwargs)
	    context['post_user'] = self.post_user

	    return context


class PostDetail(SelectRelatedMixin, generic.DetailView):
	'''  Post detail view '''

	model = models.Post
	select_related = ('user', 'group')

	def get_queryset(self):
		''' Fetches the post details for a particular user's post '''

		queryset = super().get_queryset()
		return queryset.filter(user__username__iexact=self.kwargs.get('username'))


class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
	''' Creates a new user post '''

	fields = ('message', 'group')
	model = models.Post

	def form_valid(self, form):
		''' Overriding method, checks if new post form data is valid '''

		self.objects = form.save(commit=False)
		self.objects.user = self.request.user
		self.objects.save()

		return super().form_valid(form)


class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
	''' Deletes a user post '''

	model = models.Post
	select_related = ('user', 'group')
	success_url = reverse_lazy('posts:all')

	def get_queryset(self):

		queryset = super().get_queryset()
		return queryset.filter(user_id = self.request.user.id)

	def delete(self, *args, **kwargs):
		messages.success(self.request, 'Post Deleted')
		return super().delete(*args, **kwargs)


from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, 								  DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm


###############  POSTS CBVs ###############


class AboutView(TemplateView):
	''' Renders the about view template, when the assoicated url is requested '''

	template_name = 'about.html'


class PostListView(ListView):
	''' Renders the post list view template, when the associated url is requested and populates it with the required data from the model '''

	model = Post

	def get_queryset(self):
		''' Use django's ORM to query data from the model. Fetch all posts that are published today or previous and sort them starting with newest. '''

		# See Django docs: Field Lookups equivalent to SQL queries
		# __lte:less than or equal to, -published:the dash means in descending order (default:asc)

		return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
	''' Renders the post list detail view template, when the assoicated url is requested and populates it with the required data from the model '''

	# Link the view to the required model, the view url has a regular expression to fetch the details of the required post based on it's primary key value 'pk' passed in the url.
	model = Post


class CreatePostView(LoginRequiredMixin, CreateView):   # Uses mixins
	''' Allows a logged in user to create a new post '''

	login_url = '/login/'  	# Set up the login url
	redirect_field_name = 'blog/post_detail'   # Redirect to post_details after creation (model abs url)
	form_class = PostForm   # Serve up the post creation form
	model = Post


class PostUpdateView(LoginRequiredMixin, UpdateView):
	''' Allows a logged in user to edit a post '''

	login_url = '/login/'
	redirect_field_name = 'blog/post_detail'
	form_class = PostForm
	model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
	''' Allows a logged in user to delete a post '''

	model = Post
	success_url = reverse_lazy('post_list')  # Only after successful deletion of the view, 
	# redirect back to the posts list page.

class DraftListView(LoginRequiredMixin, ListView):
	''' Renders the post list view template, when the associated url is requested and populates it with the required data from the model '''

	def get_queryset(self):
		''' Use django's ORM to query data from the model. Fetch all posts that are not yet published. '''

		return Post.objects.filter(published_date__isnull=True).order_by('create_date')


###############  COMMENTS VIEW FUNCTIONS ###############

@login_required
def add_comment_to_post(request, pk):  # primary key is to ID the post to comment on
	''' Allows a logged in user to add a comment to a particular post '''

	post = get_object_or_404(Post, pk=pk) # fetch the post or the 404 page if not found

	if request.method == 'POST':
		form = CommentForm(request.POST)  # fetch the form data and set to form object

		if form.is_valid():  # if all form validations passed
			comment = form.save(commit=False)  # Save comment but dont commit to model yet
			comment.post = post  # Link the comment to a post via foreign key relationship
			comment.save()

			return redirect('post_detail', pk=post.pk) # Invoke the post_detail url passing in the related post primary key reference. This redirects the user to the commented post.

	else:
		form = CommentForm() # Set the form object to an empty form

	return render(request, 'blog/comment_form.html', {'form': form}) # Render the comment form

@login_required
def comment_approve(request, pk):
	''' Allows a logged in user to approve a comment their particular post '''

	comment = get_object_or_404(Comment, pk=pk)  # fetch the comment by its primary key
	comment.approve()  # Approve it for publication using the approve method of the comment model

	return redirect('post_detail', pk=comment.post.pk)  # Redirect to the related post

@login_required
def comment_remove(request, pk):
	''' Allows a logged in user to delete their comment to a post '''

	comment = get_object_or_404(Comment, pk=pk)
	post_pk = comment.post.pk # Save the post pk from the comment obj before deleting it
	comment.delete()   # django model method, similat to save()

	return redirect('post_detail', pk=post_pk)

login_required
def post_publish(request, pk):
	''' Allows a user to publish a new post '''

	post = get_object_or_404(Post, pk=pk)
	post.publish()

	return redirect('post_detail', pk=pk)
















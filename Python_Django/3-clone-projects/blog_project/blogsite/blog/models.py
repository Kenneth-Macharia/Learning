from django.db import models
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
	''' Manages the posts data on the blog '''

	author = models.ForeignKey('auth.User', on_delete='models.CASCADE')  # Each post is linked to an authorization user/ owner
	title = models.CharField(max_length=200)
	text = models.TextField()
	create_date = models.DateTimeField(default=timezone.now) # Dont execute the 'now' method here!
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		''' Sets the post publish time '''
		
		self.published_date = timezone.now()
		self.save() # Commit the published time

	def approved_comments(self):
		''' Returns approved comments for publishing on blog site '''

		return self.comments.filter(approved_comment=True)

	def get_absolute_url(self):
		''' Redirects the user to the post details page after creating it using its primary key '''

		return reverse('post_detail', kwargs={'pk':self.pk})

	def __str__(self):
		''' Returns the post title when printing the post model object '''

		return self.title


class Comment(models.Model):
	''' Manages the comments data on the blog '''

	# Comments related to a post
	post = models.ForeignKey('blog.Post', related_name='comments', on_delete='models.CASCADE')  
	author = models.CharField(max_length=200)
	text = models.TextField()
	create_date = models.DateTimeField(default=timezone.now) # Dont execute the 'now' method here!
	approved_comment = models.BooleanField(default=False)

	def approve(self):
		''' Approves a comment prior to publishing on theh blog site '''

		self.approved_comment = True
		self.save()

	def get_absolute_url(self):
		''' Redirects the user to the posts list page after creating a comment '''

		return reverse('post_list')

	def __str__(self):
		''' Returns the comment when printing the comment model object '''

		return self.text




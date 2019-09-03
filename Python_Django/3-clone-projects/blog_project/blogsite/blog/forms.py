from django import forms
from .models import Comment, Post

class PostForm(forms.ModelForm):
	''' Generates the posts model form for data capture '''

	class Meta:
		''' Links the posts model to the model form '''
		
		model = Post
		fields = ('author', 'title', 'text')

		# Add widget attributes to correspond to CSS classes so that we can custom style the widgets, widgets are simply html elements e.g textareas, buttons etc.

		widgets = {

			'title': forms.TextInput(attrs={'class':'textinputclass'}),
			
			# editable and medium-editor-textarea classes are from a medium library
			'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
		}


class CommentForm(forms.ModelForm):
	''' Generates the comments model form, for data capture '''

	class Meta:
		''' Links the comments model to the model form '''
		model = Comment
		fields = ('author', 'text')

		widgets = {

			'author': forms.TextInput(attrs={'class':'textinputclass'}),
			'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
		}
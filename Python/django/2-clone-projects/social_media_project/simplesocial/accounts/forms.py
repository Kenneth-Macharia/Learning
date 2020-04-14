from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
	''' User registration form class '''

	class Meta:
		fields = ('username', 'email', 'password1', 'password2') # Default to django user model
		model = get_user_model() # get current user

	def __init__(self, *args, **kwargs):
		''' Initial form custom form labes from the view '''
		
		super().__init__(*args, **kwargs)
		self.fields['username'].label = 'Display Name' # Custom form label
		self.fields['email'].label = 'Email Address'

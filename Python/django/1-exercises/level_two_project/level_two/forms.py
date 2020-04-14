from django	import forms
from .models import User
from django.forms import ModelForm

class UserForms(forms.ModelForm):
	# Form field validation if any

	class Meta:
		model = User
		fields = ('First_name', 'Last_name', 'Email')

from django import forms
from django.core import validators

# CUSTOM VALIDATION USING DJANOG VALIDATORS
# - Say the first letter of the name field needs to be upper case, create a custom validation function to check for this condition:

# def capitalized_name_check(value):  # value parameter is the data enteres in the name field
# 	if value[0] != value[0].upper():
# 		 raise forms.ValidationError('Name must start with a capital letter')


class FormName(forms.Form):

	# name = forms.CharField(validators=[capitalized_name_check])

	name = forms.CharField()
	email = forms.EmailField()
	confirm_email = forms.EmailField()
	text = forms.CharField(widget=forms.Textarea)

	# A malicious bot may try to input junk data into you sites form by trying to manipulate the site's HTML on submit.
	# Set up a hidden botchatcher field

	# botchatcher = forms.CharField(required=False, widget=forms.HiddenInput)

	# Set up a clean method to detect bot subbotage attempts (MANUAL WAY)

	# def clean_botchatcher(self):
	# 	botchatcher = self.cleaned_data['botchatcher']

	# 	if len(botchatcher) > 0:
	# 		raise forms.ValidationError('Bot detected')

	# 	return botchatcher


	# USING DJANGO'S BUILT IN VALIDATOR (RECOMMENDED WAY) - import django's validators module and use it add a validation types to a form's input as a list.

	# botchatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[								  validators.MaxLengthValidator(0)])

	# CLEANING THE ENTIRE FORM AT ONCE: Create a clean function:
	def clean(self):
		# Call the clean methodxsxs from the super class
		all_clean_data = super().clean()

		# Specify the fields to be cleaned and clean criteria

		# NAME CAPS CHECK
		name = all_clean_data['name']
		if name[0] != name[0].upper():
			raise forms.ValidationError('Name must start with a capital letter')

		# EMAIL MATCH CHECK
		email = all_clean_data['email']
		verified_email = all_clean_data['confirm_email']

		if email != verified_email:
			raise forms.ValidationError('Email addresses do not match!')

# CHECK OUT DJANGO DOCS FOR MORE EXAMPLES ON VALIDATION.
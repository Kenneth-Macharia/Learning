from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .forms import UserForms

# Create your views here.
def index(request):
	return HttpResponse('<h2>Welcome to the level_two app</h2>\n\n<p>Go to /users to view the list of user</p>\n\n<p>Go to /register to register</p>')

def users(request):
	users = User.objects.order_by('Last_name')
	user_dict = {'page_records': users}
	return render(request, 'level_two/users.html', context=user_dict)

def user_reg(request):
	form = UserForms()

	if request.method == 'POST':
		form = UserForms(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return index(request)  # After data is saved, navigate user to home page

		else:
			print('Invalid data, check and enter again')

	return render(request, 'level_two/register.html', {'form': form})
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'level_two_project.settings')
import django
django.setup()
from faker import Faker
from level_two.models import User

fake_data_gen = Faker()

def populate_data(N=10):

	for entry in range(N):

		fake_fname = fake_data_gen.first_name()
		fake_lname = fake_data_gen.last_name()
		fake_email = fake_data_gen.ascii_free_email()

		user = User.objects.get_or_create(First_name=fake_fname, Last_name=fake_lname, Email=								  fake_email)[0]

if __name__ == '__main__':

	print('Populating fake data to database')
	populate_data()
	print('Populating complete')
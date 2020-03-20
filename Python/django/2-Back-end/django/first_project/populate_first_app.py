# THE FIRST_APP MODELS FAKE DATA POPULATON SCRIPT

# Point to the app's configs module, since this is a self running script
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

# Set up the Django framework for this script
import django
django.setup()

# Code out the script
import random  # To randomize fake data collectin from Faker
from faker import Faker  # Libary to provide fake data for the app's models
from first_app.models import AccessRecord, Topic, Webpage

# Initialize Faker
fake_data_gen = Faker()

# A list of topics for the site
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

# Function to add topics
def add_topic():
	''' Create a new topic for the Topic class '''

	topic = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
	# The get_or_create method either fetchs an object or creates it, if it does not exist. It returns a tuple of the fetched/ created object and a boolean whether the object was created or not. In this case if one of the topics in the list for topics does not already exist, it will be created.

	topic.save()  # Save new topic to db
	return topic  # For the other classes that require this object

# Function to add the fake webpages and accessrecords
def populate_data(N=5):  # Default number of pages and accessrecords to create, can be set to anything
	
	for entry in range(N):

		# fetch topic for the page
		topic = add_topic()

		# create the fake data for the page
		fake_url = fake_data_gen.url()
		fake_name = fake_data_gen.company()
		fake_date = fake_data_gen.date()

		# Create the new webpage
		web_page = Webpage.objects.get_or_create(page_topic=topic, page_url=fake_url, page_name=fake_name)[0]

		# Create an accessrecord for the new webpage
		access_record = AccessRecord.objects.get_or_create(page_accessed_name=web_page,page_accessed_date=fake_date)[0]


# Run the fake data generation script
if __name__ == '__main__':

	print('Populating fake data to database')
	populate_data() # Leave args blank to use the default value or pass desired value.
	print('Populating complete')

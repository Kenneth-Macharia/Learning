from django.db import models

# Create your models here.

class Topic(models.Model):
	''' Model class to hold webiste topic data '''

	topic_name = models.CharField(max_length=264, unique=True)

	def __str__(self):
		''' To return the topic name from the class when Print() is used on a class object '''
		return self.topic_name

class Webpage(models.Model):
	''' Model class to hold webpage info '''

	page_topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	page_url = models.URLField(unique=True)
	page_name = models.CharField(max_length=264, unique=True)

	def __str__(self):
		return self.page_name

class AccessRecord(models.Model):
	''' Model class to hold page access time logs '''

	page_accessed_name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
	page_accessed_date = models.DateField()

	def __str__(self):
		return str(self.page_accessed_date)

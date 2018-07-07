from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')

	# change the representation of object
	def __str__(self):
		return self.question_text

	# custom function
	# check if pub_date is more than or equal to one day from "today"
	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
		
class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length = 200)
	votes = models.IntegerField(default = 0)

	# change the representation of object
	def __str__(self):
		return self.choice_text
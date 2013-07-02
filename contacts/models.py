from django.db import models

class Contact(models.Model):
	first_name = models.CharField(max_length=255)
	user = models.CharField(max_length=255)
	def __str__(self):
		return self.first_name

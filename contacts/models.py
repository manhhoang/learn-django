from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    user = models.ForeignKey(User)
    first_name = models.CharField(max_length=255)
    def __str__(self):
        return self.first_name
		
    def save(self, *args, **kwargs):
	    return super(Contact, self).save(*args, **kwargs)

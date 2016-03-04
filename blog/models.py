from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
	post_title = models.CharField(max_length = 100)
	post_text = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User)


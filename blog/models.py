from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.

class Post(models.Model):
	post_title = models.CharField(max_length = 100)
	post_text = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User)
	post_slug = models.SlugField(max_length=60, blank=True)

	def save(self, *args, **kwargs):
		if not self.id:
			self.post_slug = slugify(self.post_title)

		super(Post, self).save(*args, **kwargs)




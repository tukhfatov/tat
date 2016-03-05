from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from pytils import translit
import itertools
# Create your models here.

class Post(models.Model):
	post_title = models.CharField(max_length = 100)
	post_text = models.TextField()
	post_short = models.CharField(max_length=60, blank = True)
	date_created = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User)
	post_slug = models.SlugField(max_length=20, blank=True)

	def save(self, *args, **kwargs):
		max_length = Post._meta.get_field('post_slug').max_length
		self.post_slug = original = translit.slugify(self.post_title)[:max_length]

		for x in itertools.count(1):
			if not Post.objects.filter(post_slug=self.post_slug).exclude(pk=self.id).exists():
				break
			self.post_slug = '%s-%d' % (original[:max_length - len(str(x)) - 1], x)
		super(Post, self).save(*args, **kwargs)

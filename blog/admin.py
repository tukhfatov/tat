from django.contrib import admin
from blog.models import Post
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class PostAdmin(SummernoteModelAdmin):
	pass
admin.site.register(Post, PostAdmin)

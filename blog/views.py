from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post

# Create your views here.
def index(request):

    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts':posts})

def detail(request, slug):

	post = get_object_or_404(Post, post_slug=slug)
	return render(request,'post.html', {'post': post})
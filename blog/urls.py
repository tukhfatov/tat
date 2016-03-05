from django.conf.urls import url, include

import blog.views


urlpatterns = [
    url(r'^$', blog.views.index, name='blog_index'),
    url(r'^post/(?P<slug>[-\w]+)/$', blog.views.detail, name='blog_detail'),
]

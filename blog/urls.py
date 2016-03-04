from django.conf.urls import url, include

import blog.views


urlpatterns = [
    url(r'^$', blog.views.index, name='blog_index'),
]

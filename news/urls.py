from django.conf.urls import url
from django.urls import path, include
from news.models import Articles
from django.views.generic import ListView, DetailView

urlpatterns = [
    url(r'^$',
        ListView.as_view(queryset=Articles.objects.all().order_by('-date')[:20],
                         template_name='news/posts.html')),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Articles, template_name='news/post.html')),
]

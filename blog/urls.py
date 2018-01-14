from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^posts/', views.PostList.as_view()),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove')
]

urlpatterns = format_suffix_patterns(urlpatterns)

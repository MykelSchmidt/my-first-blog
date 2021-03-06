from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^posts/', views.PostList.as_view()),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^post/(?P<pk>\d+)/like/$', views.add_like_to_post, name='add_like_to_post'),
    url(r'^createaccount/$', views.create_account, name='create_account'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),


]

urlpatterns = format_suffix_patterns(urlpatterns)

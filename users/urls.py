from . import views
from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.users_list, name='users_list'),
    
]

urlpatterns += [
    url(r'^register/$', views.register_request, name="register"),
    url(r'^my-profile/$', views.profile_view, name='profile'),
    path('profile/<slug>/', views.anyuser_profile_view, name='profile_view'),
    url(r'^friends/$', views.friend_list, name='friend_list'),
    url(r'^friend-request/send/(?P<id>\d+)/$', views.send_friend_request, name='send_friend_request'),
    url(r'^friend-request/cancel/(?P<id>\d+)/$', views.cancel_friend_request, name='cancel_friend_request'),
    url(r'^friend-request/accept/(?P<id>\d+)/$', views.accept_friend_request, name='accept_friend_request'),
    url(r'^friend-request/delete/(?P<id>\d+)/$', views.delete_friend_request, name='delete_friend_request'),
    url(r'^friend/delete/(?P<id>\d+)/$', views.delete_friend, name='delete_friend'),
    url(r'^search_users/$', views.search_users, name='search_users'),
]


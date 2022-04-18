from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^recover/(?P<signature>.+)/$', views.recover_done,
            name='password_reset_sent'),
    re_path(r'^recover/$', views.recover, name='password_reset_recover'),
    re_path(r'^reset/done/$', views.reset_done, name='password_reset_done'),
    re_path(r'^reset/(?P<token>[\w:-]+)/$', views.reset,
            name='password_reset_reset'),
]

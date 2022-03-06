from django.urls import path

from forgot_password import views

urlpatterns = [
    path('', views.recover_password),
]

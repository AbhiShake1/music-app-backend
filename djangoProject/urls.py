from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api=create_user/', include('create_user.urls')),
    path('api=signin/', include('signin.urls')),
    path('forgot_password/', include('forgot_password.urls')),
]

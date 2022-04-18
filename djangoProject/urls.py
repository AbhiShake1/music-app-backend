from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api=create_user/', include('create_user.urls')),
    path('api=signin/', include('signin.urls')),
    path('api=forgot_password/', include('password_reset.urls')),
    path('api=signout/', include('signout.urls')),
    path('api=feedback/', include('feedbacks.urls')),
    path('api=music_upload/', include('music_upload.urls')),
    path('api=request_music/', include('request_music.urls')),
    path('api=notifications/', include('notifications.urls')),
]

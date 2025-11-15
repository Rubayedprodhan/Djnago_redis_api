from django.urls import path
from .views import register_user, upload_video, video_status

urlpatterns = [
    path('register/', register_user),
    path('upload/', upload_video),
    path('video-status/<int:video_id>/', video_status),
]

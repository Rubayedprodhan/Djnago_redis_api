from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Video
from .Serializers import VideoSerializer
from django.core.cache import cache

# User Registration with cache example
@api_view(['POST'])
def register_user(request):
    username = request.data['username']
    email = request.data['email']
    password = request.data['password']

    user = User.objects.create_user(username=username, email=email, password=password)
    
    # Cache example
    cache.set(f"user_{user.id}_welcome", "Welcome to LMS", timeout=3600)
    
    return Response({'detail': 'User created. Welcome message cached.'})

# Video upload + cache example
@api_view(['POST'])
def upload_video(request):
    serializer = VideoSerializer(data=request.data)
    if serializer.is_valid():
        video = serializer.save()
        cache.set(f"video_{video.id}_processed", False)
        return Response({'detail': 'Video uploaded. Status cached as False.'})
    return Response(serializer.errors)

# Check video status
@api_view(['GET'])
def video_status(request, video_id):
    status = cache.get(f"video_{video_id}_processed")
    return Response({'video_id': video_id, 'processed': status})

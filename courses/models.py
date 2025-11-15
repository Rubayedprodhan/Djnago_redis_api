from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='videos/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

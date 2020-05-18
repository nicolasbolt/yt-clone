from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django.utils import timezone

class Video(models.Model):
    title = models.CharField(max_length=100)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    videoFile = models.FileField(upload_to='uploads/videoFiles', validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    thumbnail = models.FileField(default="uploads/thumbnails/thumbnail-default.jpg", upload_to='uploads/thumbnails', validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])
    date_posted = models.DateTimeField(default=timezone.now)
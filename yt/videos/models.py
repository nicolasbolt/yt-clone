from django.db import models
from django.core.validators import FileExtensionValidator

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    videoFile = models.FileField(upload_to='uploads/', validators=[FileExtensionValidator(allowed_extensions=['mp4'])])

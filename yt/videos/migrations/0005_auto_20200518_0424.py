# Generated by Django 3.0.6 on 2020-05-18 04:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_video_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='thumbnail',
            field=models.FileField(default='uploads/thumbnails/thumbnail-default.jpg', upload_to='uploads/thumbnails', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])]),
        ),
        migrations.AlterField(
            model_name='video',
            name='videoFile',
            field=models.FileField(upload_to='uploads/videoFiles', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])]),
        ),
    ]

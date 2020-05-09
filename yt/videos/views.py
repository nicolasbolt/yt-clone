from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .models import Video

class CreateVideo(CreateView):
    model = Video
    fields = ['title', 'description', 'videoFile']
    template_name = 'videos/create_video.html'

    def get_success_url(self):
        return reverse('video-detail', kwargs={'pk': self.object.pk})

class DetailVideo(DetailView):
    model = Video
    template_name = 'videos/detail_video.html'


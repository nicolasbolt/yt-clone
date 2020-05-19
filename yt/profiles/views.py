from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Profile
from videos.models import Video

class ProfileView(View):
    
    def get(self, request, pk, *args, **kwargs):
        profile = get_object_or_404(Profile, pk=pk)
        videos = Video.objects.all().filter(uploader=pk).order_by('-date_posted')

        context = {
            'profile': profile,
            'videos' : videos
        }


        return render(request, 'profiles/profile.html', context)


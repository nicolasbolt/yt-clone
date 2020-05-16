from django.shortcuts import render
from django.views import View

class ProfileView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'profiles/profile.html')

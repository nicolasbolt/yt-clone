from django.shortcuts import render
# from django.views import View
from django.views.generic.detail import DetailView
from .models import Profile

# class ProfileView(View):

#     def get(self, request, *args, **kwargs):
#         return render(request, 'profiles/profile.html')

class ProfileView(DetailView):
    model = Profile
    template_name = 'profiles/profile.html'


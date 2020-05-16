from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import UserRegisterForm
from profiles.forms import UserProfileForm

class RegisterView(View):

    def get(self, request, *args, **kwargs):

        form = UserRegisterForm()
        profile_form = UserProfileForm()
        context = {
            'form': form,
            'profile_form': profile_form,
        }
        return render(request, 'users/register.html', context)

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created For {username}.  You are now able to login!')
            return redirect('login')

        context = {
            'form': form
        }
        return render(request, 'users/register.html', context)

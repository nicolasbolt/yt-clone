from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import UserRegisterForm

class RegisterView(View):

    def get(self, request, *args, **kwargs):

        form = UserRegisterForm()
        context = {
            'form': form
        }
        return render(request, 'users/register.html', context)

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created For {username}.  You are now able to login!')
            return redirect('login')

        context = {
            'form': form
        }
        return render(request, 'users/register.html', context)

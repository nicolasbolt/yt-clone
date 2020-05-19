from django.urls import path
from . import views

urlpatterns = [
    path('user/<int:pk>', views.ProfileView.as_view(), name='profile'),
]
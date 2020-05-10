from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateVideo.as_view(), name='video-create'),
    path('<int:pk>/', views.DetailVideo.as_view(), name='video-detail'),
    path('<int:pk>/edit', views.UpdateVideo.as_view(), name='video-update'),
    path('<int:pk>/delete', views.DeleteVideo.as_view(), name="video-delete"),
]
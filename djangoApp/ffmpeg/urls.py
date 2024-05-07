from django.urls import path

from . import views

urlpatterns = [
    # ffmpeg
    path('transcode/', views.transcode),
]

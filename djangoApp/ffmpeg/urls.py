from django.urls import path

from . import views

app_name = "ffmpeg"

urlpatterns = [
    # ffmpeg
    path('transcode/', views.transcode, name="transcode"),
]

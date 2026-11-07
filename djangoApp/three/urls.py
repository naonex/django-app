from django.urls import path

from . import views

app_name = "three"

urlpatterns = [
    path('openstreetmap/', views.threeOpenstreetmap, name="threeOpenstreetmap"),
]

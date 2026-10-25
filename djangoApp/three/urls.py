from django.urls import path

from . import views

app_name = "three"

urlpatterns = [
    path('', views.index, name="index"),
    path('openstreetmap/', views.threeOpenstreetmap, name="threeOpenstreetmap"),
    path('api/image/', views.imageGet, name="imageGet"),
]

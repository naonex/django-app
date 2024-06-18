from django.urls import path

from . import views

urlpatterns = [
    # three
    path('', views.index),
    path('openstreetmap/', views.threeOpenstreetmap),
    path('api/image/', views.imageGet),
]

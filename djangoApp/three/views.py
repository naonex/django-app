from django.shortcuts import render
from django.http import HttpResponse
import requests  # NOTE: pip install requests
import base64
# ページ名一覧
from djangoApp.user_settings import PAGE_TITLES

# Create your views here.
def threeOpenstreetmap(request):
    context = {"PAGE_TITLES": PAGE_TITLES}
    response = render(request, 'three/openstreetmap.html', context)
    return response

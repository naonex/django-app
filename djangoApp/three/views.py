from django.shortcuts import render
from django.http import HttpResponse
import requests  # NOTE: pip install requests
import base64
# ページ名一覧
from djangoApp.user_settings import PAGE_TITLES

# Create your views here.
def index(request):
    context = {"PAGE_TITLES": PAGE_TITLES}
    response = render(request, 'three/index.html', context)
    return response

def threeOpenstreetmap(request):
    context = {"PAGE_TITLES": PAGE_TITLES}
    response = render(request, 'three/openstreetmap.html', context)
    return response

def imageGet(request):
    # APIのURL
    urlServer = request.GET.get("url")

    headers = {
        'Content-Type': 'image/png',
        # NOTE: python.requestsのデフォユーザーエージェントだと、スクレイピング扱いされて弾かれる？っぽいので、何かしら設定する必要あり
        'User-Agent': 'django',
    }
    proxies = {
        'http':  '',
        'https': '',
    }
    response = requests.get('https://' + urlServer, headers=headers ,proxies=proxies)

    body = response.content
    base = base64.b64encode(body)

    response = HttpResponse(base64.b64decode(base))
    response['Content-type'] = 'image/png'
    return response

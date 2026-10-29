from django.shortcuts import render
# ページ名一覧
from djangoApp.user_settings import PAGE_TITLES

# Create your views here.
def transcode(request):
    context = {"PAGE_TITLES": PAGE_TITLES}
    response = render(request, 'ffmpeg/transcode.html', context)
    # NOTE: このheaderがないとSharedArrayBufferが使えない
    response['Cross-Origin-Embedder-Policy'] = 'require-corp'
    response['Cross-Origin-Opener-Policy'] = 'same-origin'
    return response

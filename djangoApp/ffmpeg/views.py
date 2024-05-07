from django.shortcuts import render

# Create your views here.
def transcode(request):
    context = {}
    response = render(request, 'ffmpeg/transcode.html', context)
    # NOTE: このheaderがないとSharedArrayBufferが使えない
    response['Cross-Origin-Embedder-Policy'] = 'require-corp'
    response['Cross-Origin-Opener-Policy'] = 'same-origin'
    return response

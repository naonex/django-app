from django.shortcuts import render
# ページ名一覧
from djangoApp.user_settings import PAGE_TITLES

# Create your views here.
def index(request):
    context = {"PAGE_TITLES": PAGE_TITLES}
    return render(request, "home/index.html", context)

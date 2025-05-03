from django.shortcuts import render
from .models import TbladvancewordsNlEn

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def word_list(request):
    words = TbladvancewordsNlEn.objects.all()[:10]
    return render(request, 'pages/word_list.html', {'words': words})


    
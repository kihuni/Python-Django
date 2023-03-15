from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')

def counter(request):
    texts = request.GET['texts']
    amount_of_words = len(texts.split())
    return render(request, 'counter.html', {'amount':amount_of_words})



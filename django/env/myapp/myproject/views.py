from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 1
    feature1.name = 'kihuni'
    feature1.details = 'Never give up my friend'
    feature1.is_true = 'true'

    feature2 = Feature()
    feature2.id = 2
    feature2.name = 'stephen'
    feature2.details = 'Dont worry to much bro'
    feature2.is_true = 'false'
    
    features = [feature1, feature2]
    return render(request, 'index.html', {'features': features})

def counter(request):
    texts = request.POST['texts']
    amount_of_words = len(texts.split())
    return render(request, 'counter.html', {'amount':amount_of_words})



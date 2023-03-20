from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['username']
        password = request.POST['username']
        password2 = request.POST['username']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Exist')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Exist')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password dont much!')
            return redirect('register')

    return render(request, 'register.html')

def Login(request):
    return render(request, 'login.html')

def counter(request):
    texts = request.POST['texts']
    amount_of_words = len(texts.split())
    return render(request, 'counter.html', {'amount':amount_of_words})



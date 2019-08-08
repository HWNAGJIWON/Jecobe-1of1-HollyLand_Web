from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def mypage(request):
    return render(request, 'main/mypage.html')

def signin(request):
    return render(request, 'main/signin.html')

def signup(request):
    return render(request, 'main/signup.html')

def detail(request):
    return render(request, 'main/detail.html')

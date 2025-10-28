from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def page(request):
    return render(request, 'page.html')

def ji(request):
    score = request.GET.get('score', 0)
    return render(request, 'ji.html', {'score': score})

def dachangji(request):
    score = request.GET.get('score', 0)
    return render(request, 'dachangji.html', {'score': score})

def daji(request):
    score = request.GET.get('score', 0)
    return render(request, 'daji.html', {'score': score})

def zhongji(request):
    score = request.GET.get('score', 0)
    return render(request, 'zhongji.html', {'score': score})

def xiaoji(request):
    score = request.GET.get('score', 0)
    return render(request, 'xiaoji.html', {'score': score})

def zhong(request):
    score = request.GET.get('score', 0)
    return render(request, 'zhong.html', {'score': score})

def suggestion(request):
    return render(request, 'suggestion.html')
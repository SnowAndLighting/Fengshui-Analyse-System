from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest

def home(request):
    return render(request, 'home.html')

def page(request):
    return render(request, 'page.html')

def result(request):
    """Unified score processing and decision on page jumping"""
    try:
        # make sure that the score is an int
        score = int(request.GET.get('score', 0))
    except ValueError:
        # try/except not an int
        return HttpResponseBadRequest("Invalid score value.")


# jump to the right page according to the score
    if score >= 70:
        return redirect('dachangji')
    elif score >= 65:
        return redirect('daji')
    elif score >= 60:
        return redirect('zhongji')
    elif score >= 55:
        return redirect('xiaoji')
    elif score >= 30:
        return redirect('ji')
    else:
        return redirect('zhong')


# result for all pages
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

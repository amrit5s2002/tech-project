from django.shortcuts import render , HttpResponse

# Create your views here.

def home(request):
    return render(request, 'test.html')


def bchain(request):
    return render(request, 'bchain.html')

def ar(request):
    return render(request, 'ar.html')

def nlp(request):
    return render(request, 'nlp.html')

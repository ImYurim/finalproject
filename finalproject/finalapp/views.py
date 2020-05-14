from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'finalapp/home.html')


def competitor(request):
    return render(request, 'finalapp/competitor.html')


def patent(request):
    return render(request, 'finalapp/patent.html')

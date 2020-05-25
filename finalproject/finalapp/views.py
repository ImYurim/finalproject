from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .models import Company
# Create your views here.


def home(request):
    return render(request, 'finalapp/home.html')


def competitor(request):
    return render(request, 'finalapp/competitor.html')


def competitorresult(request):
    if 'company' in request.GET and request.GET['company']:
        company = request.GET['company']
        companyname = Company.objects.filter(
            name=company)
        if companyname:
            return render(request, 'finalapp/competitorresult.html', {'companyname': companyname, 'company': company})
        else:
            return render(request, 'finalapp/competitor.html', {'error': True})
    else:
        return render(request, 'finalapp/competitor.html', {'error': True})


def searchpatent(request):
    if request.GET.get('company'):
        companyname = request.GET.get('company')
        companydetail = Company.objects.all().filter(name="companyname")
        return render(request, 'finalapp/patent.html', {'companydetail': companydetail})
    else:
        return render(request, 'finalapp/patent.html')

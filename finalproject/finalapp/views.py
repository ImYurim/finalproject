from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .models import Company
# Create your views here.


def home(request):
    return render(request, 'finalapp/home.html')


def competitor(request):
    companyall = Company.objects.all()
    return render(request, 'finalapp/competitor.html', {'companyall': companyall})


def competitorresult(request):
    if 'company' in request.GET and request.GET['company']:
        company = request.GET['company']
        companydetail = Company.objects.all().filter(
            name=company)
        if companydetail:
            return render(request, 'finalapp/competitorresult.html', {'companydetail': companydetail, 'company': company})
        else:
            companyall = Company.objects.all()
            return render(request, 'finalapp/competitor.html', {'error': True, 'companyall': companyall})
    else:
        companyall = Company.objects.all()
        return render(request, 'finalapp/competitor.html', {'error': True, 'companyall': companyall})


def searchpatent(request):
    if request.GET.get('company'):
        companyname = request.GET.get('company')
        companydetail = Company.objects.all().filter(name="companyname")
        return render(request, 'finalapp/patent.html', {'companydetail': companydetail})
    else:
        return render(request, 'finalapp/patent.html')

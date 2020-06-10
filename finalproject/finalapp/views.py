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
            mycompany = Company.objects.get(name=company)
            competitor1_name = mycompany.competitor1
            competitor1 = Company.objects.get(name=competitor1_name)
            competitor1_strength = [competitor1.strength1, competitor1.strength2,
                                    competitor1.strength3, competitor1.strength4, competitor1.strength5]
            mycompany_strength = [mycompany.strength1, mycompany.strength2,
                                  mycompany.strength3, mycompany.strength4, mycompany.strength5]
            similar1 = []
            for s in mycompany_strength:
                if s in competitor1_strength:
                    similar1.append(s)

            return render(request, 'finalapp/competitorresult.html', {'companydetail': companydetail, 'company': company, 'similar1': similar1})
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

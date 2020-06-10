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

            competitor2_name = mycompany.competitor2
            competitor2 = Company.objects.get(name=competitor2_name)
            competitor2_strength = [competitor2.strength1, competitor2.strength2,
                                    competitor2.strength3, competitor2.strength4, competitor2.strength5]

            similar2 = []
            for s in mycompany_strength:
                if s in competitor2_strength:
                    similar2.append(s)

            competitor3_name = mycompany.competitor3
            competitor3 = Company.objects.get(name=competitor3_name)
            competitor3_strength = [competitor3.strength1, competitor3.strength2,
                                    competitor3.strength3, competitor3.strength4, competitor3.strength5]

            similar3 = []
            for s in mycompany_strength:
                if s in competitor3_strength:
                    similar3.append(s)

            competitor4_name = mycompany.competitor4
            competitor4 = Company.objects.get(name=competitor4_name)
            competitor4_strength = [competitor4.strength1, competitor4.strength2,
                                    competitor4.strength3, competitor4.strength4, competitor4.strength5]

            similar4 = []
            for s in mycompany_strength:
                if s in competitor4_strength:
                    similar4.append(s)

            competitor5_name = mycompany.competitor5
            competitor5 = Company.objects.get(name=competitor5_name)
            competitor5_strength = [competitor5.strength1, competitor5.strength2,
                                    competitor5.strength3, competitor5.strength4, competitor5.strength5]

            similar5 = []
            for s in mycompany_strength:
                if s in competitor5_strength:
                    similar5.append(s)

            return render(request, 'finalapp/competitorresult.html', {'companydetail': companydetail, 'company': company, 'similar1': similar1, 'similar2': similar2, 'similar3': similar3, 'similar4': similar4, 'similar5': similar5})
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

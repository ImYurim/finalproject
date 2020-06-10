from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .models import Company, Patent
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

            competitor1_s = []
            competitor1_w = []
            for i in competitor1_strength:
                patent1 = Patent.objects.get(name=competitor1_name, patent=i)
                mycom = Patent.objects.get(name=company, patent=i)
                if patent1.number > mycom.number:
                    competitor1_s.append(i)
                else:
                    competitor1_w.append(i)

            competitor2_s = []
            competitor2_w = []
            for i in competitor2_strength:
                patent1 = Patent.objects.get(name=competitor2_name, patent=i)
                mycom = Patent.objects.get(name=company, patent=i)
                if patent1.number > mycom.number:
                    competitor2_s.append(i)
                else:
                    competitor2_w.append(i)

            competitor3_s = []
            competitor3_w = []
            for i in competitor3_strength:
                patent1 = Patent.objects.get(name=competitor3_name, patent=i)
                mycom = Patent.objects.get(name=company, patent=i)
                if patent1.number > mycom.number:
                    competitor3_s.append(i)
                else:
                    competitor3_w.append(i)

            competitor4_s = []
            competitor4_w = []
            for i in competitor4_strength:
                patent1 = Patent.objects.get(name=competitor4_name, patent=i)
                mycom = Patent.objects.get(name=company, patent=i)
                if patent1.number > mycom.number:
                    competitor4_s.append(i)
                else:
                    competitor4_w.append(i)

            competitor5_s = []
            competitor5_w = []
            for i in competitor5_strength:
                patent1 = Patent.objects.get(name=competitor5_name, patent=i)
                mycom = Patent.objects.get(name=company, patent=i)
                if patent1.number > mycom.number:
                    competitor5_s.append(i)
                else:
                    competitor5_w.append(i)

            patent_valid = mycompany.patent_valid
            cpp = round(mycompany.cpp, 3)
            pii = round(mycompany.pii, 3)
            ts = round(mycompany.ts, 3)
            patent_avg = (competitor1.patent_valid + competitor2.patent_valid +
                          competitor3.patent_valid + competitor4.patent_valid + competitor5.patent_valid) / 5
            patent_avg = round(patent_avg, 3)
            cpp_avg = (competitor1.cpp + competitor2.cpp +
                       competitor3.cpp + competitor4.cpp + competitor5.cpp)/5
            cpp_avg = round(cpp_avg, 3)
            pii_avg = (competitor1.pii + competitor2.pii +
                       competitor3.pii + competitor4.pii + competitor5.pii) / 5
            pii_avg = round(pii_avg, 3)
            ts_avg = (competitor1.ts + competitor2.ts +
                      competitor3.ts + competitor4.ts + competitor5.ts)/5
            ts_avg = round(ts_avg, 3)
            return render(request, 'finalapp/competitorresult.html', {'companydetail': companydetail, 'company': company, 'similar1': similar1, 'similar2': similar2, 'similar3': similar3, 'similar4': similar4, 'similar5': similar5, 'patent_valid': patent_valid, 'cpp': cpp, 'pii': pii, 'ts': ts, 'patent_avg': patent_avg, 'cpp_avg': cpp_avg, 'pii_avg': pii_avg, 'ts_avg': ts_avg, 'competitor1_s': competitor1_s, 'competitor1_w': competitor1_w, 'competitor2_s': competitor2_s, 'competitor2_w': competitor2_w, 'competitor3_s': competitor3_w, 'competitor4_s': competitor4_s, 'competitor4_w': competitor4_w, 'competitor5_s': competitor5_s, 'competitor5_w': competitor5_w})
        else:
            companyall = Company.objects.all()
            return render(request, 'finalapp/competitor.html', {'error': True, 'companyall': companyall})
    else:
        companyall = Company.objects.all()
        return render(request, 'finalapp/competitor.html', {'error': True, 'companyall': companyall})


def searchpatent(request):
    companyall = Company.objects.all()
    return render(request, 'finalapp/patent.html', {'companyall': companyall})


def patentresult(request):
    if 'company' in request.GET and request.GET['company']:
        company = request.GET['company']
        companydetail = Company.objects.all().filter(
            name=company)
        if companydetail:
            mycompany = Company.objects.get(name=company)
            return render(request, 'finalapp/patentresult.html', {'companydetail': companydetail, 'company': company})
        else:
            companyall = Company.objects.all()
            return render(request, 'finalapp/patent.html', {'error': True, 'companyall': companyall})
    else:
        companyall = Company.objects.all()
        return render(request, 'finalapp/patent.html', {'error': True, 'companyall': companyall})

    return render(request, 'finalapp/patentresult.html')

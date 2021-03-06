"""finalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import finalapp.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', finalapp.views.home, name="home"),
    path('competitor/', finalapp.views.competitor, name="competitor"),
    path('competitorresult/', finalapp.views.competitorresult,
         name="competitorresult"),
    path('patent/', finalapp.views.searchpatent, name="searchpatent"),
    path('patentresult/', finalapp.views.patentresult, name="patentresult"),
    path('patentexplain/', finalapp.views.patentexplain, name="patentexplain"),
    path('patentselect/', finalapp.views.patentselect, name="patentselect"),
    path('dictionary/', finalapp.views.dictionary, name="dictionary"),
]

from django.db import models


# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=300)
    strength1 = models.CharField(max_length=100)
    strength2 = models.CharField(max_length=100)
    strength3 = models.CharField(max_length=100)
    strength4 = models.CharField(max_length=100)
    strength5 = models.CharField(max_length=100)
    competitor1 = models.CharField(max_length=400)
    competitor2 = models.CharField(max_length=400)
    competitor3 = models.CharField(max_length=400)
    competitor4 = models.CharField(max_length=400)
    competitor5 = models.CharField(max_length=400)
    strength1_avg = models.FloatField()
    strength2_avg = models.FloatField()
    strength3_avg = models.FloatField()
    strength4_avg = models.FloatField()
    strength5_avg = models.FloatField()
    mycompany_strength1 = models.IntegerField()
    mycompany_strength2 = models.IntegerField()
    mycompany_strength3 = models.IntegerField()
    mycompany_strength4 = models.IntegerField()
    mycompany_strength5 = models.IntegerField()
    patent_valid = models.FloatField()
    cpp = models.FloatField()
    pii = models.FloatField()
    ts = models.FloatField()

    def __str__(self):
        return self.name


class Patent(models.Model):
    name = models.CharField(max_length=300)
    patent = models.CharField(max_length=100)
    number = models.IntegerField()

    def __str__(self):
        return self.name

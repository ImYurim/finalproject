# Generated by Django 3.0.5 on 2020-06-24 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('patent_num', models.IntegerField()),
                ('strength1', models.CharField(max_length=100)),
                ('strength2', models.CharField(max_length=100)),
                ('strength3', models.CharField(max_length=100)),
                ('strength4', models.CharField(max_length=100)),
                ('strength5', models.CharField(max_length=100)),
                ('competitor1', models.CharField(max_length=400)),
                ('competitor2', models.CharField(max_length=400)),
                ('competitor3', models.CharField(max_length=400)),
                ('competitor4', models.CharField(max_length=400)),
                ('competitor5', models.CharField(max_length=400)),
                ('strength1_avg', models.FloatField()),
                ('strength2_avg', models.FloatField()),
                ('strength3_avg', models.FloatField()),
                ('strength4_avg', models.FloatField()),
                ('strength5_avg', models.FloatField()),
                ('mycompany_strength1', models.IntegerField()),
                ('mycompany_strength2', models.IntegerField()),
                ('mycompany_strength3', models.IntegerField()),
                ('mycompany_strength4', models.IntegerField()),
                ('mycompany_strength5', models.IntegerField()),
                ('patent_valid', models.FloatField()),
                ('cpp', models.FloatField()),
                ('pii', models.FloatField()),
                ('ts', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='IPC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patent', models.CharField(max_length=100)),
                ('explain', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Patent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('patent', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Patentdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patent', models.CharField(max_length=100)),
                ('patentnumber', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('representative', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=50)),
                ('independentclaimnumber', models.IntegerField()),
                ('totalclaimnumber', models.IntegerField()),
                ('quotation', models.IntegerField()),
                ('citation', models.IntegerField()),
                ('valid', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=600)),
                ('familypatentnumber', models.IntegerField()),
                ('impact', models.FloatField()),
                ('transfer', models.FloatField()),
                ('promising', models.FloatField()),
            ],
        ),
    ]

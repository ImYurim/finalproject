# Generated by Django 3.0.5 on 2020-06-23 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0002_ipc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patentdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patent', models.CharField(max_length=100)),
                ('patentnumber', models.IntegerField()),
                ('date', models.CharField(max_length=200)),
                ('representative', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=50)),
                ('independentclaimnumber', models.IntegerField()),
                ('totalclaimnumber', models.IntegerField()),
                ('quotation', models.IntegerField()),
                ('citation', models.IntegerField()),
                ('valid', models.CharField(max_length=100)),
                ('familypatentnumber', models.IntegerField()),
                ('impact', models.FloatField()),
                ('transfer', models.FloatField()),
                ('promising', models.FloatField()),
            ],
        ),
    ]
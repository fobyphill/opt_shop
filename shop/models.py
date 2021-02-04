from django.contrib.auth.models import AbstractUser
from django.db import models

class genders(models.Model):
    gender = models.CharField(max_length=1, primary_key=True)
    description = models.CharField(max_length=7)

class client(models.Model):
    inn = models.CharField(max_length=12, primary_key=True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20)
    mail = models.CharField(max_length=50)
    birthday = models.DateField()
    gender = models.ForeignKey(genders, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)

class contracts(models.Model):
    id_contract = models.AutoField(primary_key=True)
    client = models.ForeignKey(client, on_delete=models.CASCADE)
    tovar_dogovor = models.FloatField()
    potrebnost = models.FloatField()
    rezerv_ojidaniya = models.FloatField()
    rezerv_na_sklade_v_puti = models.FloatField()
    otlojen_dolg = models.FloatField()
    VD = models.FloatField()
    VO = models.FloatField()
    kursovaya_raznica = models.FloatField()
    dengi_dogovor = models.FloatField()
    tovar_otgruzka = models.FloatField()
    descripton = models.CharField(max_length=255)

class user(AbstractUser):
        inn = models.CharField(max_length=12, default='123456789')
        gender = models.ForeignKey(genders, on_delete=models.CASCADE, default='m')



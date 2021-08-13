from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name= models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)
    cin     = models.IntegerField()
    username= models.CharField(max_length=30,unique=True)   
    password= models.CharField(max_length=30)   
    codeQR  = models.CharField(max_length=30)
    poste   = models.CharField(max_length=30)
    image   = models.CharField(max_length=30)
    email   = models.EmailField()
    telephone= models.IntegerField()
    is_superuser=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


class pointage(models.Model):
    entre   = models.CharField(max_length=30)
    sortie  = models.CharField(max_length=30)
    retard  = models.CharField(max_length=30)
    absance = models.CharField(max_length=30)   
    user    = models.ManyToManyField(User)


class salaire(models.Model):
    mois      = models.IntegerField()
    heurs_base= models.FloatField()
    heurs_sup = models.FloatField()
    primes    = models.FloatField()  
    total     = models.FloatField()   
    user    = models.ManyToManyField(User)



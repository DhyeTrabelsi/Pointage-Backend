from django.contrib import admin

# Register your models here.
from employes.models import *

admin.site.register(User)
admin.site.register(pointage)
admin.site.register(salaire)
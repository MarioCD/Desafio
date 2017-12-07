from django.db import models
from django.contrib import admin

# Create your models here.

class CadUsu(models.Model):
    Usuario = models.CharField(max_length=50)
    Senha = models.CharField(max_length=6)
    

class CadUsuAdmin(admin.ModelAdmin):
   list_display = ('Usuario','Senha')

admin.site.register(CadUsu, CadUsuAdmin)

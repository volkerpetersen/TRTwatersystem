"""
---------------------------------------------------------------------
TRT_watersystem Admin with the database definitions

https://pythonprogramming.net/django-web-development-python-tutorial/

 
site admin page: volker.petersen01@gmail.com Forte123

https://docs.djangoproject.com/en/3.1/intro/tutorial07/
---------------------------------------------------------------------
"""
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Watersystem

admin.site.unregister(Group)

class WatersystemAdmin(admin.ModelAdmin):
    list_display = ('date', 'LodgeWater', 'SouthWater', 'NorthWater', 'LodgeElectricity', 'SouthElectricity', 'NorthElectricity')
    ordering = ('-date',)

admin.site.register(Watersystem, WatersystemAdmin)

admin.site.site_header = "TRT Watersystem Database Administration"

"""
---------------------------------------------------------------------
TRT_watersystem Models with the database definitions
 
site admin page: TRTadmin forte

add existing tables to model.py
$: python manage.py inspectdb > test.py and copy relevant tables to
   models.py

   python manage.py makemigrations
   python manage.py migrate
---------------------------------------------------------------------
"""
from django.db import models
#from django.contrib.auth.models import User

class Watersystem(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(help_text="date in YYYY-MM-DD format")
    LodgeWater = models.IntegerField(help_text="Lodge Well Water Meter Reading in gallons")
    SouthWater = models.IntegerField(help_text="South Well Water Meter Reading in gallons")
    NorthWater = models.IntegerField(help_text="North Well Water Meter Reading in gallons")
    LodgeElectricity = models.IntegerField(help_text="Lodge Well Electricity Meter Reading in kWh")
    SouthElectricity = models.IntegerField(help_text="South Well Electricity Meter Reading in kWh")
    NorthElectricity = models.IntegerField(help_text="North Well Electricity Meter Reading in kWh")
    notes = models.CharField(max_length=255, blank=True,
                             help_text="any notes...")

    def __str__(self):
        return f"{self.date}: {self.LodgeWater} - {self.LodgeElectricity} | {self.SouthWater} - {self.SouthElectricity} | {self.NorthWater} - {self.NorthElectricity} | "

    class Meta:
        managed = False
        db_table = 'Watersystem'
        verbose_name_plural = 'Watersystem'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

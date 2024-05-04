from django.db import models

# Create your models here.
class Reservation(models.Model):
    date_reservation=models.DateField()
    class Meta:
        db_table="Reservation"
        


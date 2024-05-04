from django.db import models

# Create your models here.
class Touriste(models.Model):
    firstname = models.CharField(max_length=50)
    lastname =models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    
    class Meta:
        db_table ="Touriste"
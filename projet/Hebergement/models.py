from django.db import models
from  destinations.models import Destination
# Create your models here.
class Hebergement(models.Model):
    name = models.CharField(max_length=100)
    type_hebergement = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='photos/%y/%m/%d', null=False,blank=False)
    class Meta:
        db_table="Hebergement"
        ordering = ['name']

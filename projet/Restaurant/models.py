from django.db import models
from  destinations.models import Destination
# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    type_cuisine = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='photos/%y/%m/%d', null=False,blank=False)
    class Meta:
        db_table="Restaurant"
        ordering = ['name']

from django.db import models

# Create your models here.
class Attraction(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='photos/%y/%m/%d', null=False,blank=False)
    class Meta:
        db_table="Attraction"
        ordering = ['name']
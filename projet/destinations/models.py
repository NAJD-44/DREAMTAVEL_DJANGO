from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='photos/%y/%m/%d', null=False,blank=False)
    class Meta:
        db_table="Destination"
        ordering = ['name']
        
    def _str_(self):
        return self.name
    
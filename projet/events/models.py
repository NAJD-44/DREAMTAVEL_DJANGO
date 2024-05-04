from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=50, null=False,blank=False)
    description = models.TextField()
    location = models.TextField( null=False,blank=False)
    image = models.ImageField(upload_to='photos/%y/%m/%d', null=False,blank=False)
    price = models.FloatField(default=0)
    def __str__(self):
        return self.title
    
    class Meta:
        db_table="Event"
        ordering=['title']
    

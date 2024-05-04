from django.db import models

# Create your models here.
class Experience(models.Model):
    commentaire = models.TextField()
    rating = models.FloatField()
    class Meta:
        db_table="Experience"
       

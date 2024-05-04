from django.db import models

# Create your models here.
class Promotion(models.Model):
    titre = models.CharField(max_length=50)
    description = models.TextField()
    validite = models.DateField()
    class Meta:
        db_table="Promotion"
        ordering = ['titre']

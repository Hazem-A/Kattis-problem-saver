from django.db import models

# Create your models here.
class lists(models.Model):
    name = models.CharField(max_length=300)



class question(models.Model):
    list = models.ForeignKey(lists,on_delete=models.CASCADE)
    Kattis_id = models.CharField(max_length=300)
    link = models.URLField(max_length=300)
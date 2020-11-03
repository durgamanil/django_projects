from django.db import models

# Create your models here.

class shirts(AppConfig):
    shirt_name=models.CharField(max_length=250)
    shirt_size=models.IntegerField()
    shirt_name=models.CharField(max_length=250)





from django.db import models
import datetime

# Create your models here.

now = datetime.datetime.now()

class People(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    birth_year = models.IntegerField(default= now.strftime('%Y'))
    birth_month = models.IntegerField(default= now.strftime('%m'))
    birth_day = models.IntegerField(default= now.strftime('%d'))
    
    def __str__(self):
        return self.first_name
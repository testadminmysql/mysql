from django.db import models


class employees(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200,blank=False, default='')
    last_name = models.CharField(max_length=200,blank=False, default='')
    email = models.CharField(max_length=200, blank=False, default='')
    phone_number = models.CharField(max_length=200,blank=False, default='')
    hire_date = models.CharField(max_length=200,blank=False, default='')
    
    
from django.db import models

class Customers(models.Model):
    customer_id = models.CharField(max_length=200)
    customer_pw = models.CharField(max_length=200)
    insta_id = models.CharField(max_length=200)
    insta_pw = models.CharField(max_length=200)
# 고객
# Create your models here.

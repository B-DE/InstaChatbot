from django.db import models
from login.models import Customers

class CustomerCollections(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    posts_id = models.CharField(max_length=200)
    # 사진 추가

class PostAnalysis(models.Model):
    post = models.ForeignKey(CustomerCollections, on_delete=models.CASCADE)
    store_id = models.CharField(max_length=200)
    store_name = models.CharField(max_length=200)
    store_sector = models.CharField(max_length=200)
    store_area = models.CharField(max_length=200)
    store_adjective_id = models.CharField(max_length=200)

class Adjective(models.Model):
    adjective_id = models.ForeignKey(PostAnalysis, on_delete=models.CASCADE)
    adjective = models.CharField(max_length=200)

class Store(models.Model):
    store = 
# 고객 컬렉션, 게시글 분석, 수식어, 업소
# Create your models here.

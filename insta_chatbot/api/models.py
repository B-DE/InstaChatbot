from django.db import models

class Customers(models.Model):    
  name = models.CharField(max_length=64)
  customer_id = models.CharField(max_length=64, primary_key=True)
  password = models.CharField(max_length=64)
  instagram_id = models.CharField(max_length=64)
  instagram_pw = models.CharField(max_length=64)

  def __str__(self):
      return [self.id, self.name, self.customer_id, self.password, self.instagram_id, self.instagram_pw]


# 데이터 분석팀이 만든 테이블로 맞출 것
class Collections(models.Model):
  customers_id = models.ForeignKey(customers, on_delete=models.CASCADE)
  post_id = models.IntegerField(primary_key=True)
#   images = models.models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
  
  def __str__(self):
      return [self.id, self.customer_id, self.post_id, self.images]


# 데이터 분석팀이 만든 테이블로 맞출 것
class Post_analysis(models.Model):
  post_id = models.ForeignKey(collections, on_delete=models.CASCADE)
  busness_name = models.ForeignKey(business)
  sector = models.CharField(max_length=64)
  region = models.CharField(max_length=64)
  modifier = models.ForeignKey(modifier)

  def __str__(self):
      return [self.id, self.post_id, self.business_id, self.busness_name, self.sector, self.region, self.modifier_id]
  

# 데이터 분석팀이 만든 테이블로 맞출 것
class Modifier(models.Model):
  modifier_id = models.IntegerField(primary_key=True)
  modifier = models.CharField()
 
  def __str__(self):
      return [self.id, self.modifier, self.modifier]


# 데이터 분석팀이 만든 테이블로 맞출 것
class Business(models.Model):
  business_id = models.IntegerField(primary_key=True)
  address = models.CharField(max_length=64)
  call_number = models.CharField(max_length=64)

  def __str__(self):
      return [self.id, self.business_id, self.address, self.call_number]

class customers(models.Model):

  id = models.IntegerField()

  name = models.CharField(max_length=64)

  customer_id = models.CharField(max_length=64)

  password = models.CharField(max_length=64)

  instagram_id = models.CharField(max_length=64)

  instagram_pw = models.CharField(max_length=64)



class collections(models.Model):

  id = models.IntegerField()

  customer_id = models.CharField(max_length=64)

  post_id = models.IntegerField()

  images = models.CharField(max_length=64)



class post_analysis(models.Model):

  id = models.IntegerField()

  post_id = models.CharField(max_length=64)

  business_id = models.IntegerField()

  busness_name = models.CharField(max_length=64)

  sector = models.CharField(max_length=64)

  region = models.CharField(max_length=64)

  modifier_id = models.IntegerField()

  

class modifier(models.Model):

  id = models.IntegerField()

  modifier_id = models.IntegerField()

  modifier = models.CharField()

 

class business(models.Model):

  id = models.IntegerField()

  business_id = models.IntegerField()

  address = models.CharField(max_length=64)

  call_number = models.CharField(max_length=64)
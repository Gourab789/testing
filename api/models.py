from django.db import models

# Create your models here.
class employee(models.Model):
      email=models.CharField(primary_key=True,max_length=256)
      firstname=models.CharField(max_length=100)
      lastname=models.CharField(max_length=100)
      mobno=models.CharField(max_length=100)
      password=models.CharField(max_length=100)
      
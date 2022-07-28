from django.db import models

# Create your models here

class Product(models.Model):
    name=models.CharField(max_length=10)
    email=models.EmailField(default='')

    def __str__(self):
        return self.email

class Signup(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    mobile_no=models.IntegerField()
    password=models.CharField(max_length=8)

    def __str__(self):
        return self.email

class Pro(models.Model):
    name=models.CharField(max_length=50)
    des=models.TextField()
    price=models.IntegerField()
    img=models.ImageField(upload_to='pro')
    review=models.TextField()

    def __str__(self):
        return self.name


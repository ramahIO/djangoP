from django.db import models

class Book(models.Model):
    title   = models.CharField(max_length = 50)
    author  = models.CharField(max_length = 50)
    price   = models.FloatField(default = 0.0)
    edition = models.SmallIntegerField(default = 1)

#11
class Address(models.Model):
    city = models.CharField(max_length=50)

class Student(models.Model):
    name    = models.CharField(max_length=50)
    age     = models.IntegerField(default=0)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)    


class Address2(models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city

class Student2(models.Model):
    name    = models.CharField(max_length=50)
    age     = models.IntegerField(default=0)
    address = models.ManyToManyField(Address2)

    def __str__(self):
        return self.name    


class Product(models.Model):
    name  = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
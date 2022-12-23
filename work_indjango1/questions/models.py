from django.db import models
from django.forms import ModelForm
# Create your models here.
class Services(models.Model):
    title = models.CharField(max_length=100, verbose_name="имя студента")
    text =  models.CharField(max_length=100, verbose_name="время посещения")

    def __str__(self):
        return self.title


class Feddback(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    text = models.CharField(max_length=100)

class Fullfb(models.Model):
    name2 = models.CharField(max_length=100)
    email2 = models.CharField(max_length=100)
    text2 = models.CharField(max_length=100)

class Staff(models.Model):
    name= models.CharField(max_length=100)
    position= models.CharField(max_length=100)
    photo=  models.ImageField(upload_to="photo/staff")
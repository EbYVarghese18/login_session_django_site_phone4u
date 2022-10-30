from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Phones(models.Model):
    p_image = models.ImageField(upload_to='phoneimages')
    p_name = models.CharField(max_length=100)
    p_description = models.TextField()

class Tablets(models.Model):
    t_image = models.ImageField(upload_to='phoneimages')
    t_name = models.CharField(max_length=100)
    t_description = models.TextField()

class Watches(models.Model):
    w_image = models.ImageField(upload_to='phoneimages')
    w_name = models.CharField(max_length=100)
    w_description = models.TextField()
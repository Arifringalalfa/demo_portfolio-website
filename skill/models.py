from datetime import datetime
from distutils.command.upload import upload
from email import message
from multiprocessing import Value
from operator import concat
from turtle import title
from django.db import models


class Myskill(models.Model):

    image = models.ImageField(upload_to='skillimage/')
    title = models.CharField(max_length=50, blank=False)
    desc = models.TextField(max_length=500, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def summary(self):
        return self.desc[0:200]

    def __str__(self):
        return self.title


class Contact(models.Model):
    cname = models.CharField(max_length=50, blank=False)
    cemail = models.EmailField(max_length=50, blank=False)
    cquery = models.TextField(max_length=500, blank=False)
    
    def __str__(self):
        return self.cname

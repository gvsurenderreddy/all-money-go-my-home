from django import forms
from django.db import models                                               
from django.contrib import admin

class User(models.Model):
    Username=models.CharField(max_length=100,unique=True)
    Password=models.CharField(max_length=20)
    Email=models.EmailField()

    def __unicode__(self):
        return self.Username

admin.site.register(User)
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tester(models.Model):
    text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date_tested')

class CoffeePic(models.Model):
    image = models.FileField(upload_to="uploads/", null=True, blank=True)
    processed_image = models.CharField(null=True, blank=True, max_length = 255)
    upload_date = models.DateTimeField('date_uploaded', auto_now_add=True)
    name = models.CharField(null=True, blank=True, max_length=255)
    processed = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.name

class CoffeeTag(models.Model):
    tag = models.CharField(max_length = 255, db_index=True)
    pic = models.ForeignKey(CoffeePic, on_delete = models.CASCADE)

    def __str__(self):
        return self.tag

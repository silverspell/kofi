# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .utils import *

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

class Customer(models.Model):
    SINGLE = "S"
    MARRIED = "M"
    DIVORCED = "D"
    ENGAGED = "E"
    PLATONIC = "P"
    UNKNOWN = "U"
    MARITALS = (
            (UNKNOWN, "Unknown"),
            (SINGLE, "Single"),
            (MARRIED, "Married"),
            (DIVORCED, "Divorced"),
            (ENGAGED, "Engaged"),
            (PLATONIC, "Platonic"),
    )

    PRIMARY = "PRI"
    MIDDLE = "MID"
    HIGH = "HIG"
    UNI = "UNI"
    POST = "POS"
    DR = "DOR"
    LEFT = "LEF"
    PHD = "PHD"
    UNKNOWN = "UNK"
    GRADUATES = (
        (UNKNOWN, "Unknown"),
        (PRIMARY, "Primary"),
        (MIDDLE, "Middle"),
        (HIGH, "High"),
        (UNI, "Univercity"),
        (POST, "Post Grad"),
        (DR, "Doctorate"),
        (PHD, "Phd"),
        (LEFT, "Left"),
    )
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255, db_index = True)
    premium_member = models.BooleanField(db_index = True, default = False)
    birthdate = models.DateField()
    birthsign = models.CharField(blank=True, null=True, max_length = 50)
    marital = models.CharField(max_length = 1, choices = MARITALS, default=UNKNOWN, db_index = True)
    graduation = models.CharField(max_length = 3, choices = GRADUATES, default = UNKNOWN, db_index = True)
    profession = models.CharField(max_length = 255, blank = True, null = True)
    credits = models.DecimalField(default = 3, max_digits = 10, decimal_places = 2)

    def __str__(self):
        return self.email
    def save(self, *args, **kwargs):
        bs = BirthSign()
        self.birthsign = bs.calculate_birthsign(self.birthdate)[0]
        super(Customer, self).save(*args, **kwargs)


class Fortune(models.Model):
    customer = models.ForeignKey("Customer", on_delete = models.CASCADE)
    pic = models.ForeignKey("CoffeePic", on_delete = models.CASCADE)
    date_submit = models.DateTimeField("date_submitted", auto_now_add = True)
    date_processed = models.DateTimeField("date_processed", null=True)
    processed = models.BooleanField(default = False, db_index = True)
    fortune_predicted = models.TextField(blank = True, null=True)



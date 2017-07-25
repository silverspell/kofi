# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import *

from datetime import datetime

class CoffeePicInline(admin.StackedInline):
    model = CoffeeTag

class CoffeePicAdmin(admin.ModelAdmin):
    model = CoffeePic
    list_display = ("name", "processed", "image_display", "found_image", "get_tags")
    inlines = [CoffeePicInline,]
    def get_processed(self, obj):
        return obj.processed
    def image_display(self, obj):
        return "<a href='/{0}'><img height='50' src='/{0}'/></a>".format(obj.image.url)
    def found_image(self, obj):
        return "<a href='/{0}'><img height='50' src='/{0}'/></a>".format(obj.processed_image)
    def get_tags(self, obj):
        tags = CoffeeTag.objects.filter(pic = obj)
        l = [i.tag for i in tags]
        return l
    image_display.allow_tags = True
    found_image.allow_tags = True

class CoffeeTagInline(admin.StackedInline):
    model = CoffeePic

class CoffeeTagAdmin(admin.ModelAdmin):
    model = CoffeeTag
    list_display = ("tag", "count", "pics")
    def get_queryset(self, request):
        qs = super(CoffeeTagAdmin, self).get_queryset(request)
        qs = qs.order_by("tag").distinct("tag")
        return qs

    def count(self, obj):
        return CoffeeTag.objects.filter(tag=obj.tag).count()
    def pics(self, obj):
        pics = set([i.pic.name for i in CoffeeTag.objects.filter(tag = obj.tag)])
        return [i for i in pics]

class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    list_display = ("name", "email", "premium_member", "credits")

class FortuneAdmin(admin.ModelAdmin):
    model = Fortune
    list_display = ("customer", "date_submit", "processed")

#admin.site.register(Tester)
admin.site.register(CoffeeTag, CoffeeTagAdmin)
admin.site.register(CoffeePic, CoffeePicAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Fortune, FortuneAdmin)

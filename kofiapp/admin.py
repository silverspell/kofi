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
    list_display = ("name", "processed", "get_tags")
    inlines = [CoffeePicInline,]
    def get_processed(self, obj):
        return obj.processed
    def get_tags(self, obj):
        tags = CoffeeTag.objects.filter(pic = obj)
        l = [i.tag for i in tags]
        return l

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


#admin.site.register(Tester)
admin.site.register(CoffeeTag, CoffeeTagAdmin)
admin.site.register(CoffeePic, CoffeePicAdmin)

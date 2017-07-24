# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .forms import *
from .models import *
import uuid

def handle_uploaded_file(f, name):
    with open("uploads/" + name, "wb+") as dest:
        for chunk in f.chunks():
            dest.write(chunk)

# Create your views here.
def index(request):
    template = loader.get_template('kofiapp/hello.html')
    text = "Hello!"
    context = {
        'a': 'Deneme 123'
    }
    return HttpResponse(template.render(context, request))

def test_json(request):
    d = {"a": 1, "b": 2, "c": {"s": "a"}, "d": [1,2,3,4]}
    return JsonResponse(d)

def echo_json(request, echovar):
    d = {"echo": echovar}
    return JsonResponse(d)

def handle_post(request):
    d = {}
    d["data"] = request.POST.get("data", "")
    f = request.FILES["file"]
    fname = str(uuid.uuid4()) + ".jpg"
    handle_uploaded_file(f, fname)
    c = CoffeePic()
    c.image = "uploads/" + fname
    c.name = fname
    c.processed = False
    c.save()
    return JsonResponse(d)

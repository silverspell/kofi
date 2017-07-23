from django.core.management.base import BaseCommand, CommandError
from kofiapp.models import *
import os
import KofiPy as kofi

class Command(BaseCommand):
    help = "Send files to Cognitive"

    def add_arguments(self, parser):
        pass


    def handle(self, *args, **options):
        coffeepics = CoffeePic.objects.filter(processed = False)
        args = {}
        BASE_DIR = os.path.abspath(".")
        d = {}
        for pic in coffeepics:
            args["image"] = BASE_DIR + "/" + pic.image.url
            args["show"] = "N"
            args["log"] = "N"
            args["return"] = "Y"
            j, fileName = kofi.main(args)
            for i in j["description"]["tags"]:
                tag = CoffeeTag(pic=pic, tag=i)
                tag.save()
            for i in j["categories"]:
                tag = CoffeeTag(pic = pic, tag = i["name"])
                tag.save()
            for i in j["tags"]:
                tag = CoffeeTag(pic = pic, tag = i["name"])
                tag.save()
            pic.processed = True
            pic.save()

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
            try:
                j, fileName = kofi.main(args)
                pic.processed_image = fileName
                tags = set()
                for i in j["description"]["tags"]:
                    tags.add(i)
                for i in j["categories"]:
                    tags.add(i["name"])
                for i in j["tags"]:
                    tags.add(i["name"])
                for i in tags:
                    tag = CoffeeTag(tag = i, pic = pic)
                    tag.save()
            finally:
                pic.processed = True
                pic.save()

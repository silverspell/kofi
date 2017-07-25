# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *

from datetime import datetime, date

class  BirthSign():
    signs = (
        ("OGLAK", "Oglak"),
        ("KOVA", "Kova"),
        ("BALIK", "Balik"),
        ("KOC", "Koc"),
        ("BOGA", "Boga"),
        ("IKIZLER", "Ikizler"),
        ("YENGEC", "Yengec"),
        ("ASLAN", "Aslan"),
        ("BASAK", "Basak"),
        ("TERAZI", "Terazi"),
        ("AKREP", "Akrep"),
        ("YAY", "Yay"),
    )

    def calculate_birthsign(self, bd):
        d = bd.day
        m = bd.month
        if (m == 12 and d >= 22) or (m == 1 and d < 22):
            return self.signs[0]
        elif (m == 1 and d >= 22) or (m == 2 and d < 20):
            return self.signs[1]
        elif (m == 2 and d >= 20) or (m == 3 and d < 21):
            return self.signs[2]
        elif (m == 3 and d >= 21) or (m == 4 and d < 21):
            return self.signs[3]
        elif (m == 4 and d >= 21) or (m == 5 and d < 22):
            return self.signs[4]
        elif (m == 5 and d >= 22) or (m == 6 and d < 23):
            return self.signs[5]
        elif (m == 6 and d >= 23) or (m == 7 and d < 22):
            return self.signs[6]
        elif (m == 7 and d >= 22) or (m == 8 and d < 23):
            return self.signs[7]
        elif (m == 8 and d >= 23) or (m == 9 and d < 23):
            return self.signs[8]
        elif (m == 9 and d >= 23) or (m == 10 and d < 23):
            return self.signs[9]
        elif (m == 10 and d >= 23) or (m == 11 and d < 22):
            return self.signs[10]
        elif (m == 11 and d >= 22) or (m == 12 and d < 22):
            return self.signs[11]

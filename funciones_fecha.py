# -*- encoding: utf8 -*-

from datetime import date

def fecha_actual():
    d = date.today()
    return " %s - %s - %s " % (d.day, d.month, d.year)

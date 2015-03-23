# -*- encoding: utf8 -*-

print("Comparador de años")

fecha1=int(input("¿En que año estamos?:"))
fecha2=int(input("Escriba un año cualquiera:"))

if fecha1 > fecha2:
    print("Desde el año %s han pasado %s años" % (fecha2, (fecha1-fecha2))

if fecha1 < fecha2:
    print("Para llegar al año %s faltan %s años" % (fecha2, (fecha2-fecha1))

if fecha1 == fecha2:
    print("¡Son el mismo año!")




# -*- encoding: utf8 -*-

print "Comparador de años"

fecha1=int(raw_input("¿En que año estamos?:"))
fecha2=int(raw_input("Escriba un año cualquiera:"))


"""
La siguiente parte utiliza sentencias condicionales
encadenadas (el orden no es importante):
"""

if fecha1 > fecha2:
    print("Desde el año %s han pasado %s años" % (fecha2, (fecha1-fecha2)))
elif fecha1 < fecha2:
    print("Para llegar al año %s faltan %s años" % (fecha2, (fecha2-fecha1)))
else:
    print("¡Son el mismo año!")

"""
El siguiente programa es para la diferencia entre fechas de un año
"""

if fecha1 - fecha2 == 1:
    print("Desde el año %s han pasado 1 año " % (fecha2))
elif fecha1 > fecha2:
    print("Desde el año %s han pasado %s años " % (fecha2, fecha1-fecha2))
elif fecha1 - fecha2 == -1:
    print("Para llegar al año %s falta 1 año " % (fecha2))
elif fecha1 < fecha2:
    print("Para llegar al año %s faltan %s años " % (fecha2, fecha2-fecha1))
else:
    print("¡Son el mismo!")


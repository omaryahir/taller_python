# -*-  encoding:utf-8 -*-

#import finanzas
from finanzas import calcularImpuesto as ci
#from finanzas import *

# función que devuelve un valor
def totalizarCompra(item1, item2):
    costoTotal = item1 + item2
    return costoTotal

articulo1 = float(raw_input("Precio número 1: "))
articulo2 = float(raw_input("Precio número 2: "))
iva = int(raw_input("% iva: "))

total1 = totalizarCompra(articulo1, articulo2)
#total2 = finanzas.calcularImpuesto(float(total1), iva)
#total2 = calcularImpuesto(float(total1), iva)
total2 = ci(float(total1), iva)

print "\n Total sin IVA = " + str(total1)
print "\n Total con IVA = " + str(total2)


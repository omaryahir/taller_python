# -*- encoding: utf8 -*-

from funciones_fecha import fecha_actual


print fecha_actual()


def totalizarcompra():
    costoTotal = articulo1 + articulo2
    print " totalizarcompra: %s " % costoTotal

articulo1 = 10
articulo2 = 30
totalizarcompra()


def totalizarCompra2(prod1, prod2):
    costoTotal = prod1 + prod2
    print " totalizarcompra2 %s " % costoTotal

articulo3=100
articulo4=200
totalizarCompra2(articulo3, articulo4)


def totalizarcompra3(item1, item2):
   costoTotal = item1 + item2
   return costoTotal

articulo1 = 10
articulo2 = 40
articulo3 = 5
articulo4 = 25

print " totalizarcompra3: %s " % (totalizarcompra3(articulo1,articulo2))
print " totalizarcompra3: %s " % (totalizarcompra3(articulo3,articulo4))



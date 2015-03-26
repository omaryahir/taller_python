# -*- coding: utf8 -*-

def calcularImpuesto(precio, impuesto):
    precioNuevo = precio / 100 * (100+impuesto)
    return precioNuevo

def calulaDescuento(preciod, descuento):
    precioDescuento = preciod - descuento
    return precioDescuento

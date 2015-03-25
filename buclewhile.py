# -*- encoding:utf8 -*-

lista = []
nombre = "inicio"

while nombre != "":
    nombre = raw_input("Escriba un nombre:")
    if nombre != "":
        telefono = raw_input("Escriba un teléfono:")
        contacto = {"nombre":nombre, "telefono": telefono}
        #lista.append(contacto)
        lista += [contacto]


print lista 

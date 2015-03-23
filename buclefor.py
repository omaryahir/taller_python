# -*- encoding:utf8 -*-

dato = int(raw_input("Escriba un número:"))
dato2 = int(raw_input("Escriba un número igual o mayor que %s :" % (dato)))

if dato2 < dato:
    print(" ¡Le he pedido un número entero mayor o igual que %s : %s ! " % (dato,dato2))
elif dato2 >= dato:
    for m in range(dato,(dato2+1)):
        if m % 2 == 0: 
            print "El número %s es par " % m
        else:
            print "El número %s es impar " % m

    

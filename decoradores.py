def avisar(f):    
    def inner(*args, **kwargs):
        f(*args, **kwargs)
        print "<Se ha ejecutado %s>" % f.__name__
    return inner 


@avisar
def abrir_puerta():
    print "Abrir la puerta"

@avisar
def cerrar_puerta():
    print "Cerrar la puerta"


abrir_puerta()
cerrar_puerta()

class mascota:
    patas = 0
    color = None

    def dormir(self):
        print 'zzzz'

class domestico:
    
    def saluda(self):
        print 'hola hola'


class perro(mascota, domestico):
    pass

#p = perro()
#p.dormir()
#p.saluda()

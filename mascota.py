class Mascotas(object):
    def __init__(self, nombre):
        self.nombre = nombre 

        def obtener_nombre(self):
            print 'Dentro de la primera Clase'
            return '{nombre}'.format(nombre=self.nombre)

class Perro(Mascotas):
    def __init__(self, nombrePerro):
        self.nombrePerro = nombrePerro

    def obtener_nombre(self):
        return self.nombrePerro                

class Gato(Mascotas):
    def __init__(self, nombreGato):
        self.nombreGato = nombreGato

    def obtener_nombre(self):
        return self.nombreGato

class Domesticos(Perro, Gato):
    A = 'un Attributo'

    def __init__(self, tipo, semejanza):
        super(Domesticos, self).__init__(semejanza)
        self.tipo = tipo

    def obtener_tipo(self):
        return self.tipo

    def obtener_semejanza(self):
        print 'Metodo de mismo comportamiento'
        semejanza = super(Domesticos, self).obtener_semejanza()
        print semejanza
        return semejanza        

if __name__ == '__main__':
    nombrePerro = Perro('krauser')
    nombreGato = Gato('kuro') 
    print nombrePerro.obtener_nombre()
    print nombreGato.obtener_nombre()

    mascota = Domesticos('Mascotas', 'Se Odian a muerte')
print mascota.obtener_nombre()
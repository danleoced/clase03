class Persona:
    def saludo(self):
        print('Hola')

    def comer(self, param1, param2):
        print('Persona comiendo')


class Peruano(Persona):
#    pass
    def saludo(self):
        print('Hablaaa')

    def comer(self):
        print('El peruano come rico.')

class Chileno(Persona):
    def saludo(self):
        print('Hola gallo')

persona = Persona()
persona.saludo()
persona.comer(1,2)

peruano = Peruano()
peruano.saludo()
peruano.comer()

chileno = Chileno()
chileno.saludo()

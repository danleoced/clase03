
class Felino:
    def __init__(self):
        print('Se creó un felino')

    def rugido(self):
        print('El felino dio un rugido')


class Mascota:
    def __init__(self):
        print('Se creo una mascota')

    def sientate(self):
        print('La mascota se sentó')


class Gato (Felino, Mascota):
    def __init__(self, energia, hambre):
        super().__init__()
        self.energia = energia
        self.hambre = hambre
        print('Se creó un gato.')

    def __str__(self):
        return 'Garfield'

    def dormir(self, horas):
        self.energia += horas
        print('El gato toma una siesta de', horas, 'horas.')

gato=Gato(10,10)
print(gato)
gato.dormir(2)
gato.rugido()
gato.sientate()
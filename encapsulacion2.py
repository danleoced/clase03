class ClaseOtroEjemplo:
    def __init__(self):
        self.publico = 'Público'
        self.__privado = 'Privado'

    def setPrivado(self, valor):
        self.__privado = valor

    def getPrivado(self):
        return self.__privado

x = ClaseOtroEjemplo()
print(x.publico)
x.publico = 'Cambio en Público'
print(x.publico)

print(x.getPrivado())
x.setPrivado('Cambio en Privado')
print(x.getPrivado())
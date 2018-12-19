class ClaseEjemplo:
    def publico(self):
        print('Método público')

    def __privado(self):
        print('Método privado')

ejemplo = ClaseEjemplo()
ejemplo.publico()
#ejemplo.__private()
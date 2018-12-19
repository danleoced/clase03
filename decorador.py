def decorador(funcion):
    def funcion_envoltura():
        print('Antes de la función')
        funcion()
        print('Después de a función')

    return funcion_envoltura


@decorador
def funcionPrueba():
    print('Hola función prueba')


funcionPrueba()
# decorador(funcionPrueba())

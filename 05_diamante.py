class A:
    def llamada(self):
        print('Llamada de A')


class B(A):
    def llamada(self):
        print('Llamada de B')
        super().llamada()


class C(A):
    def llamada(self):
        print('Llamada de C')
        super().llamada()


class D(C, B):
    def llamada(self):
        print('Llamada de D')
        super().llamada()
        #B.llamada(self)
        #C.llamada(self)


d = D()
d.llamada()
def decor(func):
    def wrap():
        print('='*12)
        func()
        print('=' * 12)

    return wrap

def decor2(f):
    def xxx():
        f()
        print('Decorador 2')

    return xxx


@decor2
@decor
def print_text():
    print('Hola Mundo')

print_text()

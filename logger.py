def log(debug):
    def _log(f):
        def wrap(a, b):
            if debug:
                print('Valor de a:', a)
                print('Valor de b:', b)

            return f(a, b)
        return wrap
    return _log

@log(debug=True)
def suma(a, b):
    return a + b

print(suma(1, 2))
class Calculadora:
    def __init__(self, numero):
        self.n = numero
        self.datos = [0 for i in range(self.n)]
    def ingresarDatos(self):
        self.datos = [int(input('Ingresar el dato número '+str(i+1)+' = ')) for i in range(self.n)]

class Op_Basica(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2)

    def suma(self):
        a,b = self.datos
        s = a + b
        print('El resultado es: ', s)

    def resta(self):
        a,b = self.datos
        r = a - b
        print('El resultado es: ', r)

class Raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1)

    def cuadrada(self):
        import math
        a = self.datos
        print('El resultado es: ', math.sqrt(a))

ejemplo = Op_Basica()
print(ejemplo.ingresarDatos())
print(ejemplo.suma())

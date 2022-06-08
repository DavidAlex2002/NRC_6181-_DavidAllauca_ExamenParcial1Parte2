class calculo:
    """
    Una clase para crear cálculos
    ........................................
    Atributos
    ----------------------------------------
    entero : int
    -------------
    Métodos
    ----------------------------------------
    constructor(self,entero)
    factorial()
    suma()
    testPrimo()
    test(Primos)
    """
    def __init__(self, entero):
        #Construye los atributos del objeto calculo
       self.entero=entero

    def factorial(entero):
        facto=[]
        print(input("Escriba un número para calcular su factorial: ", entero))
        for i in range(entero):
               """
               #Condicional for
               #Asigna los valores de acuerdo al numero seleccionado previamente
               """
               print("EL factorial de: ", entero, "N°", str(i+1)," es :", end="")
               valor=int(1)
               facto+=[valor] 
    def suma(self,entero):
        pass
    def testPrimo(self,entero):
        pass
    def testPrimos(self, entero):
        pass
    def tableMult(self,entero):
        pass
    def TablaMultiplicar(self,entero):
        pass
    def listDiv(self,entero):
        pass
    def listDivPrim(self,entero):
        pass

p=calculo(1)
print(calculo)
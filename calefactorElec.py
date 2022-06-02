from claseCalefactor import  calefactor

class electrico(calefactor):
    __potencia=None
    def __init__(self,marca,modelo,potencia):
        super.__init__(marca,modelo)
        self.__potencia=potencia
    def getPotencia(self):
        return self.__potencia
    def __lt__(self, other):
        if self.getPotencia() < other.getPotencia()
            bandera=True
        else:
            bandera=False
     def __str__(self):
        cadena='{0} {1}'.format(super().getMarca(),super().getModelo())
        return cadena

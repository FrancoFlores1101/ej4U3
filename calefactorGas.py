from claseCalefactor import  calefactor

class calefactorAgas(calefactor):
    __matricula=None
    __calorias=None
    def __init__(self,marca,modelo,matricula,calorias):
        super.__init__(marca,modelo)
        self.__calorias=calorias
        self.__matricula=matricula
    def getCalorias(self):
        return self.__calorias
    def __lt__(self, other):
        if self.getCalorias() < other.getCalorias()
            bandera=True
        else:
            bandera=False
        return bandera
    def __str__(self):
        cadena='{0} {1}'.format(super().getMarca(),super().getModelo())
        return cadena

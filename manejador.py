import numpy as np
from claseCalefactor import calefactor
import csv
from calefactorElec import electrico
from calefactorGas import calefactorAgas

class Manejador:
    __dimension=5
    __cantidad=0
    __calefactores=None
    __incremento=0
    def __init__(self):
        self.__cantidad=0
        self.__incremento=5
        self.__dimension=5
        self.__calefactores=np.empty(5,dtype=calefactor)
    def agregar(self,unCalefactor):
        if self.__dimension== self.__cantidad:
            self.__dimension +=self.__incremento
            self.__calefactores.resize(self.__dimension)
        self.__calefactores[self.__cantidad]=unCalefactor
        self.__cantidad+=1
    def leercsvs(self):
        archivo=open('calefactor-electrico.csv')
        reader=csv.reader(archivo,delimiter=';')
        for row in reader:
            instancia=electrico(row[0],row[1],row[2])
            self.agregar(instancia)
        archivo=open('calefactor-a-gas.csv')
        reader=csv.reader(archivo,delimiter=';')
        for row in reader:
            instancia=calefactorAgas(row[0],row[1],row[2],row[3])
            self.agregar(instancia)
    def getPrimergas(self):
        while i < self.__cantidad and isinstance(self.__calefactores,electrico):
            i+=1
        if i== self.__cantidad
            i-1
        return i
    def menorcostogas(self,consumo):
        indicegas=self.getPrimergas()
        menor=self.__calefactores[indicegas]
        for i in range(indicegas,self.__cantidad):
            if self.__calefactores[i] < menor:
                menor=self.__calefactores[i]
        return menor
     def menorcostoelectrico(self,consumo):
        indicegas=self.getPrimergas()
        menor=self.__calefactores[indicegas-1]
        for i in range(indicegas):
            if self.__calefactores[i] < menor:
                menor=self.__calefactores[i]
        return menor


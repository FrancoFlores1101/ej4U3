from manejador import Manejador

if __name__ == '__main__':
    unmanejador=Manejador()
    unmanejador.leercsvs()
    calefactorGasmenor=unmanejador.menorcostogas()
    calefactorElectricomenor=unmanejador.menorcostoelectrico()
    print('el calefactor electrico de menor consumo es: {0}'.format(calefactorElectricomenor))
    print('el calefactor a gas de menor consumo es: {0}'.format(calefactorGasmenor))

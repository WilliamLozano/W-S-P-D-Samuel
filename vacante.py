from Ocupacion import *
from Ubicacion import *
class Vacante ():
    def __init__ (self):
        self.__numVacantes = int(input("Ingrese cuantas vacantes va abrir para la oferta: "))
        self.__salario = int(input("Ingrese el salario que va a tener el cargo: "))
        self.__experienciaMeses = int(input("Cuanta experiencia debe de tener el candidato: "))
        self.__tipoContrato = input("Ingrese el tipo de contrato con el que va a contar el candidato: ")
        self.__jornadaLaboral = int(input ("""1. Medio tiempo
        2. Todo el dia
        Digita la opcion que corresponda"""))
        self.__tipoSalario = input ("Cual sera el tipo de salario: ")
        self.__ocupacion = input ("Ingrese la ocupacion que necesita: ")
        self.__ubicacion = input ("Ingrese la ubicacion en la que va a estar: ")

    def getDatosVacantes (self):
        return f"""Los datos de la vacante son:
        Ocupacion: {self.__ocupacion}
        Numero de vacantes: {self.__numVacantes}
        Salario: {self.__salario}
        Experiencia en meses: {self.__experienciaMeses}
        Tipo de contrato: {self.__tipoContrato}
        Ubicacion: {self.__ubicacion}
        Jornada laboral: {self.__jornadaLaboral}
        Tipo de salario: {self.__tipoSalario} """




        

        
        
        




<<<<<<< HEAD
class Vacante:
    def __init__(self,ocupacion, num_vacantes, salario, experiencia, tipo_contrato, ubicacion, jornada_laboral, tipo_salario):
        self.ocupacion = ocupacion
        self.num_vacantes = num_vacantes
        self.salario = salario
        self.experiencia = experiencia 
        self.salario = salario
        self.tipo_contrato= tipo_contrato
        self.ubicacion = ubicacion
        self.jornada_laboral= jornada_laboral
        self.tipo_salario = tipo_salario
        self.vacantes = []

         
    def mostaratributos(self):
        print(self.ocupacion)
        print(f'{self.num_vacantes}')
        print(f'{self.salario}')
        print(f'{self.experiencia}')
        print(f'{self.tipo_contrato}')
        print(f'{self.ubicacion}')
        print(f'{self.jornada_laboral}')
        print(f'{self.tipo_salario}')
        print(f'{self.vacantes}')

#ejemplo de uso
vacante1 = Vacante('analista',4,1500000,5,'fijo','buenos aires','medio tiempo','normal')
vacante1.mostaratributos()




        

        
        
        



=======
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




        

        
        
        



>>>>>>> Peter

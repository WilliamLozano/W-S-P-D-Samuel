from ocupacion import *
from ubicacion import *
class Vacante ():
    def __init__ (self):
        try: 
            self.__ocupacionVacante = ""
            self.__ubicacionVacante = ""
            self.__habilidades = input ("Ingrese las habilidades que se necesitaran en el cargo: ")
            self.__competencias = input ("Ingrese las competencias que necesita en el cargo: ")
            self.__numVacantes = int (input("Ingrese cuantas vacantes va abrir para la oferta: "))
            self.__tipoSalario = input ("Ingrese cual sera el tipo de salario: ")
            self.__salario = int (input("Ingrese el salario que va a tener el cargo: "))
            self.__horario = input ("Ingrese el horario laboral: ")
            self.__manejoPersona = input ("El cargo requiere de manejo de personal (SI/NO): ")
            self.__libretaMilitar = input ("El candidato debera tener libreta militar (SI/NO): ")
            self.__experienciaMeses = int(input("Cuanta experiencia debe de tener el candidato en meses: "))
            self.__tipoContrato = input("Ingrese el tipo de contrato con el que va a contar el candidato: ")
            self.__jornadaLaboral = input ("Ingrese la jornada laboral que va a tener el cargo: ")
        except:
            print ("Usted hizo una mala movida :3")
    
    def getHabilidades (self):
        return self.__habilidades
    
    def getCompetencias (self):
        return self.__competencias
    
    def getNumVacantes (self):
        return self.__numVacantes
    
    def getTipoSalario (self):
        return self.__tipoSalario
    
    def getSalario (self):
        return self.__salario
    
    def getHorario (self):
        return self.__horario
    
    def getManejoPersona (self):
        return self.__manejoPersona
    
    def getlibretaMilitar (self):
        return self.__libretaMilitar
    
    def getExperiencia (self):
        return self.__experienciaMeses
    
    def getTipoContrato (self):
        return self.__tipoContrato
    
    def getJornada (self):
        return self.__jornadaLaboral
    
    def agregarOcupacion (self,ocupacion):
        self.__ocupacionVacante = ocupacion
        return self.__ocupacionVacante
    
    def agregarUbicacion (self,ubicacion):
        self.__ubicacionVacante = ubicacion 
        return self.__ubicacionVacante
    
    def getIdOcupacion (self):
        return self.__ocupacionVacante.getIdOcu()
    
    def getFechaOcupacion (self):
        return self.__ocupacionVacante.getFechaInscripcion()

    def getNomOcupacion (self):
        return self.__ocupacionVacante.getCargoOcu()
    
    def getCantidatosOcupacion (self):
        return self.__ocupacionVacante.getCanRequeridos()
    
    def getCodigoDepa (self):
        return self.__ubicacionVacante.getCodiDepartament()
    
    def getCodigoMuni (self):
        return self.__ubicacionVacante.getCodiMunicipio()
    
    def getNomDepa (self):
        return self.__ubicacionVacante.getNomDepartament()
    
    def getNomMuni (self):
        return self.__ubicacionVacante.getNomMunicipio ()
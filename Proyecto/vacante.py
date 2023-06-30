from Ocupacion import *
from Ubicacion import *
class Vacante ():
    def __init__ (self):
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
    
    def getDatosVacantes (self):
        return f"""
{print(self.getCargoOcu())}
-------------------------------
Habilidades: {self.__habilidades}

Competencias: {self.__competencias}

Experiencia en meses: {self.__experienciaMeses} meses             

Candidatos para entrevistar: {print(self.getCanRequeridos())}

Tipo de salario: {self.__tipoSalario} 

Tipo de contrato: {self.__tipoContrato}                            

Horario: {self.__horario}

Departamento: {print(self.getNomDepartament())}

Municipio: {print(self.getNomMunicipio())}

Manejo Personal: {self.__manejoPersona}

Libreta Militar: {self.__libretaMilitar}

Numero de vacantes: {self.__numVacantes}                        

Salario: {self.__salario}
                                              
Jornada laboral: {self.__jornadaLaboral}                      

--------------------------------"""
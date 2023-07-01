from Vacante import *
from Ocupacion import *
from Postulacion import *
class Oferta:
    ofertas = []
    def __init__(self):
        try:
            self.__id = int(input ("Ingrese el id de la oferta: "))
            self.__numPostulados = 0
            self.__fechaPublicacion = input ("Ingrese la fecha de publicación en la que publicara la oferta: ")
            self.__fechaCierre = input ("Ingrese la fecha de cierre en la que desabilitara la oferta: ")
            self.__vacante = ""
        except:
            print ("Usted hizo una mala movida :3")
        Oferta.ofertas.append(self)
        

    def getIdOfert (self):
        return self.__id
    
    def getNumPostulados (self):
        return self.__numPostulados
    
    def getFechaPublic (self):
        return self.__fechaPublicacion
    
    def getFechaCierre (self):
        return self.__fechaCierre
    
    def agregarVacante (self,vacante):
        instancia = vacante
        self.__vacante = instancia
        return self.__vacante
    
    def getCargo (self):
        return self.__vacante.getNomOcupacion()
    
    def getSalario (self):
        return self.__vacante.getSalario()
    
    def getExperiencia (self):
        return self.__vacante.getExperiencia()
    
    def getTipoContrato (self):
        return self.__vacante.getTipoContrato()
    
    def getNomDepartamento (self):
        return self.__vacante.getNomDepa()
    
    def getNomMunicipio (self):
        return self.__vacante.getNomMuni()
    
    def getNumVacantes (self):
        return self.__vacante.getNumVacantes()
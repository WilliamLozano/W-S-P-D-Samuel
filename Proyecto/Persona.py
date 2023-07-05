from Usuario import *
from vacante import *
from oferta import *
class Persona(Usuario):
    PersonasCreadas = []
    def __init__ (self, nombre):
        Usuario.__init__ (self,nombre)
        self.__apellido = input("Ingrese su apellido: ")
        self.__tipoDocumento = input("Ingrese con que tipo de documento cuenta: ")
        self.__documento = int(input("Ingrese su numero de documento: "))
        self.__estudios = input("Ingrese que estudios a tenido, si a tenido mas de uno separelo por comas: ")
        self.__direccion = input("Ingrese una dirección de residencia: ")
        self.__telefono = int(input("Ingrese su numero de télefono: "))
        self.__estadoCivil = input("Su estado civil es: ")
        self.__libretaMilitar = input("Cuenta con libreta militar (SI/NO): ")
        self.__correo = input("Ingrese su correo electronico personal: ")
        self.__postulaciones = []
        Persona.PersonasCreadas.append(self)


    def getNombre (self):
        return super().getNombre()
    
    def getApellido (self):
        return self.__apellido
    
    def getTipoDocumento (self):
        return self.__tipoDocumento
    
    def getDocumento (self):
        return self.__documento
    
    def getEstudios (self):
        return self.__estudios
    
    def getDireccion (self):
        return self.__direccion
    
    def getTelefono (self):
        return self.__telefono
    
    def getestadoCivil (self):
        return self.__estadoCivil
    
    def getLibretaMilitar (self):
        return self.__libretaMilitar
    
    def getCorreo (self):
        return self.__correo
    
    def getDatosPersona(self):
        return f"""\nSus datos como Usuario son:\n
--------------------------------
Nombre: {self.getNombre()}
Apellido: {self.__apellido}
Tipo de documento: {self.__tipoDocumento}
Documento: {self.__documento}
Estudios: {self.__estudios}
Dirección: {self.__direccion}
Teléfono: {self.__telefono}
Estado civil: {self.__estadoCivil}
Libreta Militar: {self.__libretaMilitar}
Correo: {self.__correo}
---------------------------------"""

    def setApellido (self,apellido):
        self.__apellido = apellido

    def setTipoDocumento (self,tipoDocumento):
        self.__tipoDocumento = tipoDocumento

    def setDocumento (self,documento):
        self.__documento = documento

    def setEstudios (self,estudios):
        self.__estudios = estudios

    def setDireccion (self,direccion):
        self.__direccion = direccion

    def setTelefono (self,telefono):
        self.__telefono = telefono

    def setEstadoCivil (self,estado):
        self.__estadoCivil = estado

    def setLibretaMilitar (self,libreta):
        self.__libretaMilitar = libreta

    def setCorreo (self,correo):
        self.__correo = correo

    def getPersonasList (self):
        cont = 0
        for i in Persona.PersonasCreadas:
            cont = cont + 1 
            print (f"{cont}. {i.getNombre()}")
    
    def postularse (self,oferta):
        pos = Postulacion (oferta)
        self.__postulaciones.append(pos)
    
    def getListPostulacion (self):
        return self.__postulaciones

class Postulacion:
    def __init__ (self,oferta):
        self.__oferta = oferta

    def getPersona (self):
        return self.__persona
    
    def getOferta (self):
        return self.__oferta
    
    def getCodigo (self):
        return self.__oferta.getIdOfert()
    
    def getCargoPost (self):
        return self.__oferta.getCargo()
    
    def getSalarioPost (self):
        return self.__oferta.getSalario()

    def getExperiencia (self):
        return self.__oferta.getExperiencia()

    
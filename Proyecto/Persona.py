from Usuario import *
from Vacante import *
class Persona(Usuario):
    PersonasCreadas = []
    def __init__ (self, nombre):
        Usuario.__init__ (self,nombre)
        self.__apellido = input("Ingrese su apellido:")
        self.__tipoDocumento = input("Ingrese con que tipo de documento cuenta:")
        self.__documento = int(input("Ingrese su numero de documento:"))
        self.__estudios = input("Ingrese que estudios a tenido:")
        self.__direccion = input("Ingrese su dirección de su casa/apartamento:")
        self.__telefono = int(input("Ingrese su télefono:"))
        self.__estadoCivil = input("Ingrese su estado civil:")
        self.__libretaMilitar = input("Ingrese si tiene la libreta Militar en el sistema, en caso contrario diga no:")
        self.__correo = input("Ingrese su correo personal:")
        self.__estado = input("Ingrese su estado:")
        Persona.PersonasCreadas.append(self)


    def getNombre(self):
        return super().getNombre()
    
    def getDatosPersona(self):
        return f"""Sus datos como Usuario serían:
        Nombre: {self.getNombre()}
        Apellido: {self.__apellido}
        Tipo de documento:{self.__tipoDocumento}
        Documento:{self.__documento}
        Estudios:{self.__estudios}
        Dirección:{self.__direccion}
        Teléfono:{self.__telefono}
        Estado civil:{self.__estadoCivil}
        Libreta Militar:{self.__libretaMilitar}
        Correo:{self.__correo}
        Estado:{self.__estado}"""

    def setDatosActualizados(self):
        self.__apellido = input("Ingrese su apellido: ")
        self.__tipoDocumento = input("Ingrese su tipo de documento: ")
        self.__documento = int(input("Ingrese su documento: "))
        self.__estudios = input("Ingrese sus estudios: ")
        self.__direccion = input("Ingrese su dirección: ")
        self.__telefono = int(input("Ingrese su teléfono: "))
        self.__estadoCivil = input("Ingrese su estado civil: ")
        self.__libretaMilitar = input("Ingrese si tiene libreta militar (sí/no): ")
        self.__correo = input("Ingrese su correo: ")
        self.__estado = input("Ingrese su estado: ")
        print("Datos cambiados con éxito!!")

    def getDatosActualizados (self):
        return f"""Sus datos actualizados como Usuario serían:
        Nombre: {self.getNombre()}
        Apellido: {self.__apellido}
        Tipo de documento:{self.__tipoDocumento}
        Documento:{self.__documento}
        Estudios:{self.__estudios}
        Dirección:{self.__direccion}
        Teléfono:{self.__telefono}
        Estado civil:{self.__estadoCivil}
        Libreta Militar:{self.__libretaMilitar}
        Correo:{self.__correo}
        Estado:{self.__estado}"""
        
    def postularVacante(self):
        input(f"{self.getNombre()} se ha postulado a la vacante: ")

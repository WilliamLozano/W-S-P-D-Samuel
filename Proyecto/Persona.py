from Usuario import *
class Persona(Usuario):
    def __init__ (self,nombre,apellido,tipoDocumento,documento,estudios,tipoEstudios,direccion,telefono,estadoCivil,
                  libretaMilitar,correo,estado):
        Usuario.__init__(nombre)
        self.__apellido = apellido
        self.__tipoDocumento = tipoDocumento
        self.__documento = documento
        self.__estudios = estudios
        self.__tipoEstudios = tipoEstudios
        self.__direccion = direccion
        self.__telefono = telefono
        self.__estadoCivil = estadoCivil
        self.__libretaMilitar = libretaMilitar
        self.__correo = correo
        self.__estado = estado
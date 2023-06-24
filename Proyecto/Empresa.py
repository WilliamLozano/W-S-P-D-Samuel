from Usuario import *
class Empresa (Usuario):
    def __init__ (self,nombre,id,telefono,descripcion,correo,tipo,direccion):
        Usuario.__init__ (self,nombre)
        self.__id = id
        self.__telefono = telefono
        self.__descripcion = descripcion
        self.__correo = correo
        self.__tipo = tipo
        self.__direccion = direccion

    def getDatosEmpresa (self):
        return f"""Sus datos como empresa {self.getDatosUsuario()} serian 
        Nombre: {self.getDatosUsuario()} 
        Id: {self.__id}
        Telefono: {self.__telefono}
        Descripcion: {self.__descripcion}
        Correo: {self.__correo}
        Tipo: {self.__tipo}
        Direccion: {self.__direccion}"""
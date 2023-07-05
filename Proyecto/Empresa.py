from Usuario import *
from Ocupacion import *
from Ubicacion import *
from Vacante import *
from Oferta import *

class Empresa (Usuario):
    empresasCreadas = []
    def __init__ (self,nombre):
        Usuario.__init__ (self,nombre)
        try:
            self.__id = int(input("Ingrese su id: "))
            self.__telefono = int(input("Ingrese su telefono: "))
            self.__descripcion = input ("Ingrese una descripcion como empresa: ")
            self.__correo = input("Ingrese su correo: ")
            self.__tipo = input ("Ingrese de que tipo es su empresa: ")
            self.__direccion = input ("Ingrese la direccion de su empresa: ")
            self.__vacante = []
            self.__oferta = []
        except:
            print ("Usted hizo una mala movida :3")
        Empresa.empresasCreadas.append (self)
        
    
    def getNombre(self):
        return super().getNombre()
    
    def getId (self):
        return self.__id
    
    def getTelefono (self):
        return self.__telefono
    
    def getDescrip (self):
        return self.__descripcion
    
    def getCorreo (self):
        return self.__correo
    
    def getTipo (self):
        return self.__tipo
    
    def getDirecc (self):
        return self.__direccion
    
    
    def getDatosEmpresa (self):
        return f"""\nSus datos como empresa {self.getNombre()} serian 
----------------------------
Nombre: {self.getNombre()} 
Id: {self.__id}
Telefono: {self.__telefono}
Descripcion: {self.__descripcion}
Correo: {self.__correo}
Tipo: {self.__tipo}
Direccion: {self.__direccion}
-----------------------------
"""
    
    def getEmpresasList (self):
        cont = 0
        for i in Empresa.empresasCreadas:
            cont = cont + 1 
            print (f"{cont}. {i.getNombre()}")
    
    def agregarVacante (self,vacante):
        self.__vacante.append(vacante)

    def agregarOferta (self,oferta):
        self.__oferta.append(oferta)

    def getOferta (self):
        return self.__oferta
    
    def getVacante (self):
        return self.__vacante
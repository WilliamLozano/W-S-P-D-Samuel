from Usuario import *
from Ocupacion import *
from Ubicacion import *
from Vacante import *
from Oferta import *

class Empresa (Usuario):
    empresasCreadas = []
    def __init__ (self,nombre):
        Usuario.__init__ (self,nombre)
        self.__id = int(input("Ingrese su id: "))
        self.__telefono = int(input("Ingrese su telefono: "))
        self.__descripcion = input ("Ingrese una descripcion como empresa: ")
        self.__correo = input("Ingrese su correo: ")
        self.__tipo = input ("Ingrese de que tipo es su empresa: ")
        self.__direccion = input ("Ingrese la direccion de su empresa: ")
        self.__ocupacionEmpresa = ""
        self.__ubicacionEmpresa = ""
        self.__vacanteEmpresa = ""
        Empresa.empresasCreadas.append (self)
        
    
    def getNombre(self):
        return super().getNombre()
    
    def getId (self):
        return self.__id
    
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
    
    def agregarOferta (self,oferta):
        self.__empresaOferta.append(oferta)
    
    def getListOferta (self):
        for i in self.__empresaOferta:
            print (i.GetDatosOferta())

    def agregarOcu (self,ocupacion):
        self.__ocupacionEmpresa = ocupacion
        return self.__ocupacionEmpresa
    
    def agregarUbi (self,ubicacion):
        self.__ubicacionEmpresa = ubicacion
        return self.__ubicacionEmpresa
    
    def agregarVac (self,vacante):
        self.__vacanteEmpresa = vacante
        return self.__vacanteEmpresa
        
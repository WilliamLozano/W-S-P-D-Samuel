from Usuario import *
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
        Empresa.empresasCreadas.append (self)
        self.__empresaOcupacion = []
        self.__empresaUbicacion = []
        self.__empresaVacante = []
        
    
    def getNombre(self):
        return super().getNombre()
    
    def getId (self):
        return self.__id
    
    def getDatosEmpresa (self):
        return f"""Sus datos como empresa {self.getNombre()} serian 
Nombre: {self.getNombre()} 
Id: {self.__id}
Telefono: {self.__telefono}
Descripcion: {self.__descripcion}
Correo: {self.__correo}
Tipo: {self.__tipo}
Direccion: {self.__direccion}"""
    
    def getEmpresasList (self):
        cont = 0
        for i in Empresa.empresasCreadas:
            cont = cont + 1 
            print (f"{cont}: {i.getId()}")

    def agregarOcupacion (self,ocupacion):
        self.__empresaOcupacion.append(ocupacion)
    
    def getListOcupacion (self):
        for i in self.__empresaOcupacion:
            print (i.getDatosOcupacion())

    def agregarUbicacion (self,ubicacion):
        self.__empresaUbicacion.append(ubicacion)

    def getListUbicacion (self):
        for i in self.__empresaUbicacion:
            print (i.getDatosUbicacion())
    
    def agregarVacante (self,vacante):
        self.__empresaVacante.append(vacante)

    def getListVacante (self):
        for i in self.__empresaVacante:
            print (i.getDatosVacantes())
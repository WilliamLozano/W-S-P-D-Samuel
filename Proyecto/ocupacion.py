class ocupacion:
    ocupacionEmpresa = []
    def __init__ (self):
        try:
            self.__id = int(input("Ingrese el id de la ocupacion: "))
            self.__fechaInscripcion = input("Ingrese la fecha de inscripcion: ")
            self.__cargo = input ("Ingrese el cargo: ")
            self.__candidatosRequeridos = int(input("Ingrese la cantidad de candidatos que necesita: "))
        except:
            print ("Usted hizo una mala movida :3")
        ocupacion.ocupacionEmpresa.append(self)

    def getIdOcu (self):
        return self.__id
    
    def getFechaInscripcion (self):
        return self.__fechaInscripcion
    
    def getCargoOcu (self):
        return self.__cargo
    
    def getCanRequeridos (self):
        return self.__candidatosRequeridos

    def getDatosOcupacion (self):
        return f"""
--------------------------------------
Id Ocupacion: {self.__id}
        
FechaInscripcion: {self.__fechaInscripcion}
        
Cargo: {self.__cargo}
        
Candidatos Requeridos: {self.__candidatosRequeridos}
---------------------------------------"""
            


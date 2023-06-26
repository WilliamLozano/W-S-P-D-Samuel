class Ocupacion:
    ocupacionEmpresa = []
    def __init__ (self):
        self.__id = int(input("Ingrese el id: "))
        self.__fechaInscripcion = input("Ingrese la fecha de inscripcion")
        self.__cargo = input ("Ingrese el cargo: ")
        self.__candidatosRequeridos = int(input("Ingrese la cantidad de candidatos que necesita: "))
        Ocupacion.ocupacionEmpresa.append(self)

    def getDatosOcupacion (self):
        return f"""Los datos de la ocupacion son:
        Id: {self.__id}
        FechaInscripcion: {self.__fechaInscripcion}
        Cargo: {self.__cargo}
        Candidatos Requeridos: {self.__candidatosRequeridos}"""
    


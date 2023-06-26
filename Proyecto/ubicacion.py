class Ubicacion:
    def __init__ (self):
        self.__codigoDepartamento = int(input("Ingrese el codigo del departamento: "))
        self.__codigoMunicipio = int(input("Ingrese el codigo del municipio: "))
        self.__nombreDepartamento = input("Ingrese el nombre del departamento: ")
        self.__nombreMunicipio = input("Ingrese el nombre del municipio: ")

    def getDatosUbicacion (self):
        return f"""Los datos de la ubicacion son:
        Codigo de departamento: {self.__codigoDepartamento}
        Codigo de municipio: {self.__codigoMunicipio}
        Nombre de departamento: {self.__nombreDepartamento}
        Nombre de municipio: {self.__nombreMunicipio}"""
    

class Ubicacion:
    ubicacionEmpresa = []
    def __init__ (self):
        try:
            self.__codigoDepartamento = int(input("Ingrese el codigo del departamento: "))
            self.__codigoMunicipio = int(input("Ingrese el codigo del municipio: "))
            self.__nombreDepartamento = input("Ingrese el nombre del departamento: ")
            self.__nombreMunicipio = input("Ingrese el nombre del municipio: ")
        except ValueError:
            print ("Usted hizo una mala movida :3")
        Ubicacion.ubicacionEmpresa.append(self)

    def getCodiDepartament (self):
        return self.__codigoDepartamento

    def getCodiMunicipio (self):
        return self.__codigoMunicipio

    def getNomDepartament (self):
        return self.__nombreDepartamento

    def getNomMunicipio (self):
        return self.__nombreMunicipio    

    def getDatosUbicacion (self):
        return f"""
----------------------------------------        
Codigo de departamento: {self.__codigoDepartamento}

Codigo de municipio: {self.__codigoMunicipio}

Nombre de departamento: {self.__nombreDepartamento}

Nombre de municipio: {self.__nombreMunicipio}
------------------------------------------
"""
    

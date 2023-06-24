class Usuario:
    def __init__(self,nombre):
        self.__nombre = nombre
    
    def getDatosUsuario (self):
        return self.__nombre
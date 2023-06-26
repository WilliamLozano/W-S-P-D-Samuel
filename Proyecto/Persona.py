from Usuario import *
from vacante import *
class Persona(Usuario):
    PersonasCreadas = []
    def __init__ (self, nombre):
        Usuario.__init__ (self,nombre)
        self.nombre = str(input("Ingrese su nombre al sistema. :"))
        self.apellido = str(input("Ingrese su apellido al sistema. :"))
        self.tipoDocumento = str(input("Ingrese su tipo de documento al sistema. :"))
        self.documento = int(input("Ingrese su documento al sistema. :"))
        self.estudios = str(input("Ingrese sus estudios en el sistema. :"))
        self.tipoEstudios = str(input("Ingrese los tipos de Estudio en el sistema. :"))
        self.direccion = str(input("Ingrese su dirección de su casa/apartamento en el sistema. :"))
        self.telefono = int(input("Ingrese su télefono en el sistema. :"))
        self.estadoCivil = str(input("Ingrese su estado civil en el sistema. :"))
        self.libretaMilitar = str(input("Ingrese si tiene la libreta Militar en el sistema, en caso contrario diga no. :"))
        self.correo = str(input("Ingrese su correo en el sistema. :"))
        self.estado = str(input("Ingrese su estado en el sistema. :"))
        Persona.PersonasCreadas.append(self)


    def getNombre(self):
        return super().getNombre()
    
    def getDatosPersona(self):

        return f"""Sus datos como Usuario serían {self.getNombre()}
        Nombre: {self.getNombre()} 
        Apellido: {self.apellido}
        Tipo de documento:{self.tipoDocumento}
        Documento:{self.documento}
        Estudios:{self.estudios}
        Tipo de estudios:{self.tipoEstudios}
        Dirección:{self.direccion}
        Teléfono:{self.telefono}
        Estado civil:{self.estadoCivil}
        Libreta Militar:{self.libretaMilitar}  
        Correo:{self.correo}
        Estado:{self.estado}"""
    

    def setDatosPersona(self):
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        tipoDocumento = input("Ingrese su tipo de documento: ")
        documento = int(input("Ingrese su documento: "))
        estudios = input("Ingrese sus estudios: ")
        tipoEstudios = input("Ingrese los tipos de estudio: ")
        direccion = input("Ingrese su dirección: ")
        telefono = int(input("Ingrese su teléfono: "))
        estadoCivil = input("Ingrese su estado civil: ")
        libretaMilitar = input("Ingrese si tiene libreta militar (sí/no): ")
        correo = input("Ingrese su correo: ")
        estado = input("Ingrese su estado: ")
        p1 = (nombre, apellido, tipoDocumento, documento, estudios, tipoEstudios,
                        direccion, telefono, estadoCivil, libretaMilitar, correo, estado)
        print("Datos cambiados con éxito!!")
        return p1

    def postularVacante(self):
        print(f"{self.getNombre()} se ha postulado a la vacante: ")

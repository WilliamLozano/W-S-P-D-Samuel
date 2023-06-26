class Oferta:
    
    def __init__(self):
        self.Id = int(input("Ingrese su ID en el sistema. :"))
        self.vacante = str(input("Ingrese la vacante al sistema. :")) 
        self.numeropostulados = int(input("Ingrese el numero de postulados en el sistema. :"))
        self.FechaPublicacion =(input("Ingrese la fecha de publicación de la oferta en el sistema. :"))
        self.FechaCierre = (input("Ingrese la fecha de cierre de la oferta en el sistema. :"))
        self.CandidatosaEntrevistar = int(input("Ingrese el numero de candidatos a entrevistar"))
        self.Estado = str(input("Ingrese el estado de la oferta en el sistema. :"))
        self.oferta = str(input("Ingrese la oferta en el sistema. :"))

    def GetDatosOferta(self):

        return f"""Los datos de la vacante son:
        Id: {self.Id}
        vacante: {self.vacante}
        numero de postulados: {self.numeropostulados}
        Fecha de publicacion: {self.FechaPublicacion}
        Fecha de cierre: {self.FechaCierre}
        Candidatos a entrevistar: {self.CandidatosaEntrevistar}
        Estado: {self.Estado}
        Oferta: {self.oferta} """

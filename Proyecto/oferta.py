class Oferta:
    def __init__(self, Id, vacante, numeropostulados, FechaPublicacion, FechaCierre, CandidatosaIntrevistar, Estado, oferta):
        self.Id = Id 
        self.vacante = vacante 
        self.numeropostulados = numeropostulados
        self.FechaPublicacion = FechaPublicacion
        self.FechaCierre = FechaCierre
        self.CandidatosaEntrevistar = CandidatosaIntrevistar
        self.Estado = Estado
        self.oferta = [oferta]
        self.Id = int(input("Ingrese su ID en el sistema. :"))
        self.vacante = str(input("Ingrese la vacante al sistema. :")) 
        self.numeropostulados = int(input("Ingrese el numero de postulados en el sistema. :"))
        self.FechaPublicacion =(input("Ingrese la fecha de publicación de la oferta en el sistema. :"))
        self.FechaCierre = (input("Ingrese la fecha de cierre de la oferta en el sistema. :"))
        self.CandidatosaEntrevistar = int(input("Ingrese el numero de candidatos a entrevistar"))
        self.Estado = str(input("Ingrese el estado de la oferta en el sistema. :"))
        self.oferta = str(input("Ingrese la oferta en el sistema. :"))

    


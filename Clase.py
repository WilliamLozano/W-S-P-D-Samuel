class Oferta:
    def __init__(self, Id, vacante, numeropostulados, FechaPublicacion, FechaCierre, CandidatosaIntrevistar, Estado, oferta):
        self.Id = Id
        self.vacante = vacante
        self.numeropostulados = numeropostulados
        self.FechaPublicacion = FechaPublicacion
        self.FechaCierre = FechaCierre
        self.CandidatosaIntrevistar = CandidatosaIntrevistar
        self.Estado = Estado
        self.oferta = oferta

    def mostrar_atributos(self):
        while True:
            print("1. Id")
            print("2. Vacante")
            print("3. Número de postulados")
            print("4. Fecha de Publicación")
            print("5. Fecha de Cierre")
            print("6. Candidatos a Entrevistar")
            print("7. Estado")
            print("8. Oferta")
            print("9. Salir")
            
            opcion = input("Seleccione un atributo (1-9): ")
            
            if opcion == "1":
                print("Id:", self.Id)
            elif opcion == "2":
                print("Vacante:", self.vacante)
            elif opcion == "3":
                print("Número de postulados:", self.numeropostulados)
            elif opcion == "4":
                print("Fecha de Publicación:", self.FechaPublicacion)
            elif opcion == "5":
                print("Fecha de Cierre:", self.FechaCierre)
            elif opcion == "6":
                print("Candidatos a Entrevistar:", self.CandidatosaIntrevistar)
            elif opcion == "7":
                print("Estado:", self.Estado)
            elif opcion == "8":
                print("Oferta:", self.oferta)
            elif opcion == "9":
                break
            else:
                print("Opción inválida")

# Ejemplo de uso
mi_oferta = Oferta(1, "Desarrollador Python", 10, "2023-06-01", "2023-06-30", 5, "Abierta", ["Beneficios competitivos", "Oportunidad de crecimiento"])
mi_oferta.mostrar_atributos()

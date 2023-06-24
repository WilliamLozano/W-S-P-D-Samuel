class Vacante:
    def __init__(self,ocupacion, num_vacantes, salario, experiencia, tipo_contrato, ubicacion, jornada_laboral, tipo_salario):
        self.ocupacion = ocupacion
        self.num_vacantes = num_vacantes
        self.salario = salario
        self.experiencia = experiencia 
        self.salario = salario
        self.tipo_contrato= tipo_contrato
        self.ubicacion = ubicacion
        self.jornada_laboral= jornada_laboral
        self.tipo_salario = tipo_salario
        self.vacantes = []

         
    def mostaratributos(self):
        print(self.ocupacion)
        print(f'{self.num_vacantes}')
        print(f'{self.salario}')
        print(f'{self.experiencia}')
        print(f'{self.tipo_contrato}')
        print(f'{self.ubicacion}')
        print(f'{self.jornada_laboral}')
        print(f'{self.tipo_salario}')
        print(f'{self.vacantes}')

#ejemplo de uso
vacante1 = Vacante('analista',4,1500000,5,'fijo','buenos aires','medio tiempo','normal')
vacante1.mostaratributos()




        

        
        
        




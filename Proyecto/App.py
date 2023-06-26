from Usuario import *
from Empresa import *
from ubicacion import *
from ocupacion import *
from vacante import *
from oferta import *
from Persona import *

print ("""Seleccione segun el numero\n
1. Persona
2. Empresa
""")

persona = input("Que tipo de usuario es: ")

match persona:
    case "1":
        salir = True
        while salir:
            print ("""\nOpciones que puede hacer como Usuario:
        1. Crear un usuario
        2. Ya tengo un Usuario
        """)
            opcion = input ("Que opcion desea realizar: ")
            if opcion == "1":
                nomPersona = str(input("Ingrese su nombre de Usuario. :"))
                persona = Persona(nomPersona)
                print("¡¡Persona creaada con exito!!")

            if opcion == "2":
                nombrePersona = input("¿Cual es el nombre de su usuario.? : ")
                for i in Persona.PersonasCreadas:
                    if nombrePersona == i.getNombre():
                        PersonaUso = i
                        print(f"Bienvenido Persona: {PersonaUso.getNombre()}")
                        salir = False

                    salir = True
                    while salir:
                        print ("""\nEstas son las opciones que puede hacer ya que creo un Usuario:
                        1. Ver datos de su Usuario
                        2. Cambiar los datos de su Usuario
                        3. Ver datos modificados
                        4. Postularse a una vacante
                        5. Salir
                        """)

                        opcion = input("¿Que opción desea realizar.? : ")

                        if opcion == "1":
                            print(persona.getDatosPersona())
                        
                        if opcion == "2":
                            persona.setDatosActualizados()

                        if opcion == "3":
                            print("Datos modificados:")
                            print(persona.getDatosActualizados())

                        if opcion == "4":
                            persona.postularVacante()
                        
                        if opcion == "5":
                            salir = False

    case  "2":
        salir = True
        while salir:
            print ("""\nOpciones que puede hacer como empresa:
        1. Crear una empresa
        2. Ya tengo una empresa
        """)
            opcion = input ("Que opcion desea realizar: ")

            if opcion == "1":
                nomEmpresa = input("Como se llama su empresa: ")
                empresa = Empresa(nomEmpresa)
                print ("¡¡Empresa creada con exito!!")

            if opcion == "2":
                idEmpresa = int(input("Cual es el id de su empresa: "))
                for i in Empresa.empresasCreadas:
                    if idEmpresa == i.getId():
                        empresaUso = i 
                        print (f"Bienvenido empresa: {i.getNombre()}")
                        salir = False 
                    
                    salir = True
                    while salir:
                        print ("""\nEstas son las opciones que puede hacer ya creo una empresa: 
                        1. Ver datos de su empresa
                        2. Ingresar Ocupacion
                        3. Ver datos de la ocupacion
                        4. Ingresar Ubicacion
                        5. Ver datos de la ubicacion
                        6. Crear una vacante
                        7. Ver datos vacante
                        8. Crear una oferta
                        9. Ver datos oferta
                        10. Salir
                        """) 
                        opcion = input("Que opcion desea realizar: ")

                        if opcion == "1":
                            print(empresa.getDatosEmpresa())

                        if opcion == "2":
                            ocu = Ocupacion()
                            empresa.agregarOcupacion(ocu)

                        if opcion == "3":
                            empresa.getListOcupacion()

                        if opcion == "4":
                            ubi = Ubicacion()
                            empresa.agregarUbicacion(ubi) 

                        if opcion == "5":
                            empresa.getListUbicacion()

                        if opcion == "6":
                            vac = Vacante()
                            empresa.agregarVacante(vac)

                        if opcion == "7":
                            empresa.getListVacante()
                        
                        if opcion == "8":
                            ofe = Oferta()
                            empresa.agregarOferta(ofe)
                        
                        if opcion == "9":
                            empresa.getListOferta()

                        if opcion == "10":
                            salir = False
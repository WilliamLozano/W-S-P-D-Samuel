from Usuario import *
from Empresa import *
from ubicacion import *
from ocupacion import *
from vacante import *
from oferta import *

print ("""Seleccione segun el numero\n
1. Persona
2. Empresa
""")

usuario = input("Que tipo de usuario es: ")

match usuario:
    case "1":
        print ("persona")
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
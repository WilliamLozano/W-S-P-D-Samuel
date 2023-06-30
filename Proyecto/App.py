from Usuario import *
from Empresa import *
from Ubicacion import *
from Ocupacion import *
from Vacante import *
from Oferta import *
from Persona import *

print ("""Seleccione segun el numero\n
1. Persona
2. Empresa
""")

persona = input("Que tipo de usuario es usted: ")

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
        while True:
            print ("""\nOpciones que puede hacer como empresa:\n
1. Crear una empresa
2. Ya tengo una empresa
3. Salir
        """)
            opcion = input ("Que opcion desea realizar: ")

            if opcion == "1":
                nomEmpresa = input("\nComo se llama su empresa: ")
                empresa = Empresa(nomEmpresa)
                print ("¡¡Empresa creada con exito!!")

            elif opcion == "2":
                print ("LISTA DE LAS EMPRESAS CREADAS\n")
                empresa.getEmpresasList()
                idEmpresa = int(input("\nCual es el id de su empresa: "))

                for i in Empresa.empresasCreadas:
                    if i.getId() == idEmpresa:
                        empresaUso = i 
                        print (f"\n¡¡Bienvenido al sistema {empresaUso.getNombre()}!!")
                        salir = False 
                    else:
                        print ("\n¡¡Sus datos no estan en el sistema!!")
                        continue
                    
                    while True:
                        print ("""\nEstas son las opciones que puede hacer como empresa\n
1. Ver datos de su empresa
2. Crear una vacante
3. Ver datos vacante
4. Ver datos de algo en especial
20. Crear una oferta
5. Ver datos oferta
10. Salir
                        """) 
                        opcion = input("Que opcion desea realizar: ")

                        if opcion == "1":
                            print(empresaUso.getDatosEmpresa())

                        if opcion == "2":
                            print ("\nOCUPACION\n")
                            ocu = Ocupacion ()
                            empresaUso.agregarOcu(ocu)

                            print ("\nUBICACION\n")
                            ubi = Ubicacion ()
                            empresaUso.agregarUbi(ubi)

                            print ("\nVACANTE\n")
                            vac = Vacante()
                            empresaUso.agregarVac(vac)

                            print ("\n¡¡Vacante creada con exito!!")
                            vac.agregarOcupacion(ocu)
                            vac.agregarUbicacion(ubi)

                        if opcion == "3":
                            print(f"""\nSINTESIS DE LA SOLICITUD\n
{ocu.getCargoOcu()}
----------------------------------
Habilidades:                        
{vac.getHabilidades()}                      

Competencias:                       
{vac.getCompetencias()}                     

Experiencia en meses:              
{vac.getExperiencia()} meses                          

Candidatos para entrevistar:       
{ocu.getCanRequeridos()}                  

Tipo de salario:                    
{vac.getTipoSalario()}                     

Tipo de contrato:                   
{vac.getTipoContrato()}                               

Horario:
{vac.getHorario()}

Departamento:
{ubi.getNomDepartament()}

Municipio:
{ubi.getNomMunicipio()}

Manejo de personal:
{vac.getManejoPersona()}

Libreta militar:
{vac.getlibretaMilitar()}

Numero de vacantes:
{vac.getNumVacantes()}

Jornada laboral:                    
{vac.getJornada()} 

Salario:        
{vac.getSalario()}                            
----------------------------------""""")
               
                        if opcion == "4":
                            while True:
                                print ("""
1. Ocupacion 
2. Ubicacion
3. Salir
""")
                                num = input("De que clase desea ver los datos: ")
                            
                                if num == "1":
                                    print(ocu.getDatosOcupacion())

                                if num == "2":
                                    print(ubi.getDatosUbicacion())

                                if num == "3":
                                    break
                        
                        if opcion == "8":
                            ofe = Oferta()
                            empresa.agregarOferta(ofe)
                        
                        if opcion == "9":
                            empresa.getListOferta()

                        if opcion == "10":
                            print ("Hasta luego")
                            break
            elif opcion == "3":
                break

            else:
                print ("""Lo que ingreso no es parte del menu
Vuelva a intentarlo""")


from Usuario import *
from Empresa import *
from Ubicacion import *
from Ocupacion import *
from Vacante import *
from Oferta import *
from Persona import *

while True:
    print ("""\nSeleccione segun el numero\n
1. Persona
2. Empresa
3. Salir
""")

    persona = input("Que tipo de usuario es usted: ")

    if persona == "1":
        while True:
            print ("""\nOpciones que puede hacer como Usuario:
1. Crear un usuario
2. Ya tengo un Usuario
3. Salir
        """)
            opcion = input ("Que opcion desea realizar: ")
            if opcion == "1":
                nomPersona = input("Ingrese su nombre: ")
                persona = Persona(nomPersona)
                print("¡¡Usuario creado con exito!!")

            if opcion == "2":
                print ("\nLISTA DE PERSONAS DENTRO DEL SISTEMA\n")
                persona.getPersonasList()
                numeroId = int(input("\nIngrese su numero de identificacion para acceder al sistema: "))
                for i in Persona.PersonasCreadas:
                    if i.getDocumento() == numeroId:
                        personaUso = i
                        print(f"\n¡¡Bienvenido {personaUso.getNombre()}!!\n")
                        break
                    else:
                        print ("\n¡¡Sus datos no estan en el sistema!!")
                        continue

                while True:
                        print ("""\nEstas son las opciones que puede hacer como usuario del sistema:
1. Ver sus datos personales
2. Actualizar algun dato personal
3. Buscar ofertas de trabajo
4. Postularse a una oferta
5. Ver datos de la oferta a la que se haya postulado
6. Salir
""")

                        opcion = input("Que opción desea realizar: ")

                        if opcion == "1":
                            print(personaUso.getDatosPersona())
                        
                        if opcion == "2":
                            print(f"""\nDatos que puede actualizar\n
1. Apellido
2. Tipo de documento
3. Documento
4. Estudios
5. Direccion
6. Telefono
7. Estado civil
8. Libreta militar
9. Correo
""")
                            accion = input ("Que dato desea actualizar: ")
                            if accion == "1":
                                apellido = input("Ingrese su apellido: ")
                                personaUso.setApellido (apellido)
                                print ("\n¡¡Cambio exitoso!!\n")
                            
                            if accion == "2":
                                tipo = input("Ingrese con que tipo de documento cuenta: ")
                                personaUso.setTipoDocumento (tipo)
                                print ("\n¡¡Cambio exitoso!!\n")

                            if accion == "3":
                                documento = int(input("Ingrese su numero de documento: "))
                                personaUso.serDocumento (documento)
                                print ("\n¡¡Cambio exitoso!!\n")

                            if accion == "4":
                                estudios = input("Ingrese que estudios a tenido, si a tenido mas de uno separelo por comas: ")
                                personaUso.setEstudios (estudios)
                                print ("\n¡¡Cambio exitoso!!\n")
                                
                            if accion == "5":
                                direccion = input("Ingrese una dirección de residencia: ")
                                personaUso.setDireccion (direccion)
                                print ("\n¡¡Cambio exitoso!!\n")

                            if accion == "6":
                                telefono = int(input("Ingrese su numero de télefono: "))
                                personaUso.setTelefono (telefono)
                                print ("\n¡¡Cambio exitoso!!\n")

                            if accion == "7":
                                estado = input("Su estado civil es: ")
                                personaUso.setEstadoCivil (estado)
                                print ("\n¡¡Cambio exitoso!!\n")

                            if accion == "8":
                                libreta = input("Cuenta con libreta militar (SI/NO): ")
                                personaUso.setLibretaMilitar (libreta)
                                print ("\n¡¡Cambio exitoso!!\n")

                            if accion == "9":
                                correo = input("Ingrese su correo electronico personal: ")
                                personaUso.setCorreo (correo)
                                print ("\n¡¡Cambio exitoso!!\n")

                        if opcion == "3":
                            buscador = input ("Escriba el nombre del cargo que esta buscando: ")
                            print (f"\nEstos son los cargos con el nombre {buscador}\n")
                            for i in Oferta.ofertas:
                                if i.getCargo() == buscador:
                                    print (f"""
-------------------------------
Codigo {i.getIdOfert()}\n
{i.getCargo()}
{i.getSalario()}
{i.getExperiencia()} de experiencia
Tipo de contrato: {i.getTipoContrato()}
{i.getNomDepartamento()},{i.getNomMunicipio()}
Vacantes: {i.getNumVacantes()}
Postulados: {i.getNumPostulados()}
Fecha publicacion: {i.getFechaPublic()}
Fecha cierre: {i.getFechaCierre()}
-------------------------------""")
                                else:
                                    print("\nNo hay cargos disponibles con ese nombre\n")
                        
                        if opcion == "4":
                            idOferta = int(input("Ingrese el id de la oferta a la que desea postularse: "))
                            for i in Oferta.ofertas:
                                if  i.getIdOfert() == idOferta:
                                    personaUso.postularse(i)
                                    print ("\n¡¡Postulacion exitosa!!")

                        if opcion == "5":
                            for i in personaUso.getListPostulacion():
                                print (f"""
-----------------------
Codigo {i.getCodigo()}\n
{i.getCargoPost()}
-----------------------""")
                                
                        if opcion == "6":
                            break

    if persona ==  "2":
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
3. Ver los datos de la vacante
4. Crear una oferta
5. Ver los datos de la oferta
6. Salir
                        """) 
                        opcion = input("Que opcion desea realizar: ")

                        if opcion == "1":
                            print(empresaUso.getDatosEmpresa())

                        if opcion == "2":
                            print ("\nOCUPACION\n")
                            ocu = Ocupacion ()

                            print ("\nOCUPACION\n")
                            ubi = Ubicacion ()
                        
                            print ("\nVACANTE\n")
                            vac = Vacante ()
                            print ("\n¡¡Vacante creada con exito!!")

                            vac.agregarOcupacion(ocu)
                            vac.agregarUbicacion(ubi)
                            empresaUso.agregarVacante (vac)

                        if opcion == "3":
                            for i in empresaUso.getVacante():
                                print(f"""\nSINTESIS DE LA SOLICITUD\n
{i.getNomOcupacion()}
----------------------------------
Habilidades:                        
{i.getHabilidades()}                      
Competencias:                       
{i.getCompetencias()}                     
Experiencia en meses:              
{i.getExperiencia()} meses                          
Candidatos para entrevistar:       
{i.getCantidatosOcupacion()}                  
Tipo de salario:                    
{i.getTipoSalario()}                     
Tipo de contrato:                   
{i.getTipoContrato()}                               
Horario:
{i.getHorario()}
Departamento:
{i.getNomDepa()}
Municipio:
{i.getNomMuni()}
Manejo de personal:
{i.getManejoPersona()}
Libreta militar:
{i.getlibretaMilitar()}
Numero de vacantes:
{i.getNumVacantes()}
Jornada laboral:                    
{i.getJornada()} 
Salario:        
{i.getSalario()}                            
----------------------------------""""")
                            
                        if opcion == "4":
                            oferta = Oferta ()
                            oferta.agregarVacante (vac)
                            empresaUso.agregarOferta (oferta)
                            print ("\n¡¡Oferta creada con exito!!\n")
                            
                        if opcion == "5":
                                print ("\nDATOS OFERTA")
                                for i in empresaUso.getOferta():
                                    print (f"""
-------------------------------
Codigo {i.getIdOfert()}\n
{i.getCargo()}
{i.getSalario()}
{i.getExperiencia()} de experiencia
Tipo de contrato: {i.getTipoContrato()}
{i.getNomDepartamento()},{i.getNomMunicipio()}
Vacantes: {i.getNumVacantes()}
Postulados: {i.getNumPostulados()}
Fecha publicacion: {i.getFechaPublic()}
Fecha cierre: {i.getFechaCierre()}
-------------------------------""")

                        if opcion == "6":
                            print ("Hasta luego")
                            break
            elif opcion == "3":
                break

            else:
                print ("""\nLo que ingreso no es parte del menu
Vuelva a intentarlo""")

    if persona == "3":
        break
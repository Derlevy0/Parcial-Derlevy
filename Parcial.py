import Funciones

DiccPacientes={}
Contador=1
# Utilizo la función "import" para traer la carpeta donde se encuentran las funciones que usare en el codigo
# Creo el diccionario que ire llenando con las listas y el contador que ire aumentando automáticamente para el codigo de cada paciente 
while True:
    ListaPacientes=[]
    M = Funciones.Validacion_Enteros("""Elija una de las siguientes opciones:
                                     1- Ingresar un paciente
                                     2- Informe de Afiliacion EPS
                                     3- Borrar paciente
                                     4- salir
                                     \n""")
# Creo la lista que ire llenando con los datos de los pacientes junto a el menu con una función previamente creada invocada mediante la función "import", con la intención de evitar errores humanos en la selección de un número 
    if M==1:
        Nom = input("Nombre del Paciente: ")
        Gen = Funciones.Validacion_Enteros("""Ingrese:
                                           0- Masculino
                                           1- Femenino
                                           \n""")
        Ed = Funciones.Validacion_Enteros("Ingrese la Edad del Paciente: ")
        Meno = Funciones.Validacion_Enteros("""¿Es Menopausic@?
                                            1- Si
                                            2- No
                                            \n""")
        HorLu = Funciones.Validacion_Flotantes("Cualo fue su Valor de la Hormona Lutenizante(UI/L): ")
        Fec = input("Fecha de Nacimiento: ")
        CC = Funciones.Validacion_Enteros("Documento de Identidad: ")
        Seg = Funciones.Validacion_Enteros("""Seleccione su Seguruidad Social:
                                           1- SISBEN
                                           2- EPS
                                           \n""")
        if Seg==1:
            Cod1 = Funciones.SISBEN(Seg, Contador)
            ListaPacientes.append(Nom)
            ListaPacientes.append(Cod1)
            ListaPacientes.append(Fec)
            ListaPacientes.append(Ed)
            ListaPacientes.append(HorLu)
            
        elif Seg==2:
            seg2 = Funciones.Validacion_Enteros("""Seleccione su EPS:
                                                1- Sura
                                                2- Coomeva
                                                3- Medimas
                                                4- IPS Universitaria
                                                5- Salud Total
                                                \n""")
            Cod2 = Funciones.EPS(Seg, seg2, Contador)
            ListaPacientes.append(Nom)
            ListaPacientes.append(Cod2)
            ListaPacientes.append(Fec)
            ListaPacientes.append(Ed)
            ListaPacientes.append(HorLu)
# Creo las varaiables que se iran llenando con los respectivos datos
# Algunas variables son creadas de forma estretegica para determinarles un solo valor absoluto que usare mas adelante 
# Uso los condicionales "if" y "elif" para hacer que el programa identifique que debe hacer según la opción que el usuario seleccione
# Para lo anterior creo pequeños sub-menus que me ayuda a detenerminar valores enteros que estaran guardados en las varaiables
# Segun el "if" o "elif" le pido al programa que guarde las variables en las listas del modo en que le indico dada una situación u otra
                                                
            if Gen==0:
                if Ed>18:
                    if HorLu<1.8 or HorLu>8.6:
                        Res = str("¡Inconsistente!: Se recomienda chequeo medico...")
                        ListaPacientes.append(Res)
                    else:
                        Res = str("¡Consistente!: Todo se encuentra en orden...")
                        ListaPacientes.append(Res)
                elif Ed<18:
                    if HorLu<1 or HorLu>1.8:
                        Res = str("¡Inconsistente!: Se recomienda chequeo medico...")
                        ListaPacientes.append(Res)
                    else:
                        Res = str("¡Consistente!: Todo se encuentra en orden...")
                        ListaPacientes.append(Res)
            elif Gen==1:
                if Meno==1:
                    if HorLu<14.2 or HorLu>52.3:
                        Res = str("¡Inconsistente!: Se recomienda chequeo medico...")
                        ListaPacientes.append(Res)
                    else:
                        Res = str("¡Consistente!: Todo se encuentra en orden...")
                        ListaPacientes.append(Res)
                elif Meno==2:
                    if HorLu<5 or HorLu>25:
                        Res = str("¡Inconsistente!: Se recomienda chequeo medico...")
                        ListaPacientes.append(Res)
                    else:
                        Res = str("¡Consistente!: Todo se encuentra en orden...")
                        ListaPacientes.append(Res)
                elif Ed<18:
                    if HorLu<0 or HorLu>5:
                        Res = str("¡Inconsistente!: Se recomienda chequeo medico...")
                        ListaPacientes.append(Res)
                    else:
                        Res = str("¡Consistente!: Todo se encuentra en orden...")
                        ListaPacientes.append(Res)
        DiccPacientes[CC]=ListaPacientes
                            
        print(f"Paciente {Nom} identificado con cedula {CC} ingresado exitosamente, su resultado es {Res}")
# Utilizo mas condicionales para crear ciertas restricciones dependientes de las variables "Gen", "Ed" y "Meno" previamente definidas por el usuario, con el fin de crear una nueva variable que dependa únicamente de las restricciones 
# Le pido al programa que me guarde la lista en el diccionario con la llave según la variable "CC"
    
    elif M==2:
        SM = Funciones.Validacion_Enteros("""Ingrese una de las siguientes opciones:
                                          1- Buscar Pacientes
                                          2- Ver cantidad de pacientes totales
                                          3- Ver cantidad de pacientes menores de 10
                                          4- Ver cantidad de pacientes mayores de 60
                                          \n""")
        if SM==1:
            Bus = Funciones.Validacion_Enteros("Ingrese el nuemero de identificacion del paciente: ")
            Ced = DiccPacientes.get(Bus, f"El paciente con el numero de identificacion {Bus} no se encuentra en la base de datos")
            if Ced!=f"El paciente con el numero de identificacion {Bus} no se encuentra en la base de datos":
                print(f"Nombre: {DiccPacientes[Bus][0]}")
                print(f"Codigo del Paciente: {DiccPacientes[Bus][1]}")
                print(f"Fecha de Nacimiento: {DiccPacientes[Bus][2]}")
                print(f"Edad: {DiccPacientes[Bus][3]}")
                print(f"LH: {DiccPacientes[Bus][4]}")
                print(f"Diagnostico: {DiccPacientes[Bus][5]}")
# Creo el sub meno del punto 2 del menu principal con la misma función del primero para luego seguir usando condicionales
# Le pido al usuario el numero de la variable "CC" que quiere buscar dado que esta es la que funciona como llave en el diccionario y asi mismo creo una nueva variable con este número 
# Le digo al programa que me busque en el diccionario el numero ingresado por el usuario para que me imprima la información que contiene dicho numero dado su funcionamiento en el diccionario 
# Al mismo tiempo solocito que imprima un letrero si caso tal el numero ingresado no se encontrara establecido como llave en el diccionario 
                
        elif SM==2:
            Total = len(DiccPacientes)
            print(f"Hay {Total} pacientes en el sistema")
# Uso la función "len" para que recorra el diccionario dado que la misma cuenta cada elemento llave/valor como uno solo, y asi obtengo la cantidad de pacientes 
            
        elif SM==3:
            Menores = list(filter(Funciones.Pacientes_Menores, DiccPacientes.values()))
            print(Menores)
        
        elif SM==4:
            Mayores = list(filter(Funciones.Pacientes_Mayores, DiccPacientes.values()))
            print(Mayores)

# Profe la verdad aquí ya se me acabo el tiempo dado que no tengo computador y un amigo me presto el de el mientras estabamos en la universidad pero se hizo muy tarde y no nos pudimos quedar mas tiempo
# No pude averiguar bien como se usaba la función filter asi que hice lo que pude y mucho menos tuve tiempo para mirar la validación del "datetime" y de los 3 intentos
# Como ust se dara cuenta el codigo entra en un error cuando llega a la parte de dar el resultado del paciente, es algo que me dolio muchísimo porque antes de "terminar" el código el estaba funcionando perfecto 
# y luego no se que sucedio que al final cuando lo volvi a probar dejaba de funcionar hasta ahí, y como le digo ya mo tenia tiempo de nada como para mirarlo detenidamente a ver que estaba pasando. Le agradecería muchísimo que me puidera decir cual
# fue el error o porque me dejo de funcionar hasta ahí :')
            
    elif M==3:
        Nu = Funciones.Validacion_Enteros("Ingrese el numero del paicnete que desea borrar: ")
        Va = DiccPacientes.get(Nu, "El paciente no se encuentra en el sistema...")
        if Va!="El paciente no se encuentra en el sistema...":
            DiccPacientes.pop(Nu)
            
    elif M==4:
        print("¡Gracias por usar el pograma!")
        break
                
            
        
                        
        
                
    
            
        

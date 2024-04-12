import Funciones

DiccPacientes={}
Contador=1
while True:
    ListaPacientes=[]
    M = Funciones.Validacion_Enteros("""Elija una de las siguientes opciones:
                                     1- Ingresar un paciente
                                     2- Informe de Afiliacion EPS
                                     3- Borrar paciente
                                     4- salir
                                     \n""")
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
                
        elif SM==2:
            Total = len(DiccPacientes)
            print(f"Hay {Total} pacientes en el sistema")
            
        elif SM==3:
            Menores = list(filter(Funciones.Pacientes_Menores, DiccPacientes.values()))
            print(Menores)
        
        elif SM==4:
            Mayores = list(filter(Funciones.Pacientes_Mayores, DiccPacientes.values()))
            print(Mayores)
            
    elif M==3:
        Nu = Funciones.Validacion_Enteros("Ingrese el numero del paicnete que desea borrar: ")
        Va = DiccPacientes.get(Nu, "El paciente no se encuentra en el sistema...")
        if Va!="El paciente no se encuentra en el sistema...":
            DiccPacientes.pop(Nu)
            
    elif M==4:
        print("¡Gracias por usar el pograma!")
        break
                
            
        
                        
        
                
    
            
        
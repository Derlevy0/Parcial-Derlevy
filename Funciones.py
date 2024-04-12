def Validacion_Enteros (msj):
    try:
        a = int(input(msj))
        return a
    except:
        print("Por favor ingrese solo valores numericos...")
        
def Validacion_Flotantes (msj):
    try:
        a = float(input(msj))
        return a
    except:
        print("Por favor ingrese solo valores numericos...")
        
def SISBEN(sisben, contador):
    if sisben==1:
        return(f"EPS-SISBEN-{contador}")
        contador+=1

def EPS(eps, EPS, contador):
    if eps==2:
        if EPS==1:
          return(f"EPS-Sura-{contador}")
          contador+=1
        elif EPS==2:
          return(f"EPS-Coomeva-{contador}")
          contador+=1
        elif EPS==3:
          return(f"EPS-Medimas-{contador}")
          contador+=1
        elif EPS==4:
          return(f"EPS-IPS Universitaria-{contador}")
          contador+=1
        elif EPS==5:
          return(f"EPS-Salud Total-{contador}")
          contador+=1
          
def Pacientes_Menores (edad):
    return edad <= 10

def Pacientes_Mayores (edad):
    return edad >= 60
        
        
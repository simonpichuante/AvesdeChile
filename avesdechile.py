#Autores = ["Julio Díaz Garcia", "-", "Simón Pichuante Olguín"]
import matplotlib.pyplot as plt

def lectura_datos(nombre):
    ent = open(nombre)
    datos = []
    for linea in ent:
        linea = linea.rstrip('\n')
        lista = linea.split(',')
        datos.append(lista)
    ent.close()
    return datos
"""
def lista_regiones(datos):
    regiones = set()
    try: 
        datos_abiertos = open(datos, 'r')
        dat = datos_abiertos.readlines()
        datos_abiertos.close
        for linea in dat:
            inf = linea.strip().split(',')
            if len(inf) > 2:
                regiones.add(inf[2])
    except FileNotFoundError:
        print(f"El archivo {datos} no se encuentra.")
    except Exception as e:
        print(f"Se ha producido un error: {e}")           
    return list(regiones)
"""
"""
def funcion_a(datos):
        datos = open('aves.txt', 'r')
        ddd = datos.read()
        aves_muertas_por_region = {}
        #lineas = str (datos.splitlines())
        for linea in ddd:    
            datos = linea.strip().split(',')
            region = datos[2]
            total_muertes = datos[7]
            if region in aves_muertas_por_region:
                aves_muertas_por_region[region] += total_muertes
            else:
                aves_muertas_por_region[region] = total_muertes
        datos.close()
        ok = ddd.splitlines()
        print(ok)
        

        return aves_muertas_por_region
#nombre_archivo = 'aves.txt'
#a = funcion_a(nombre_archivo)


#for region, cantidad in a.items():
#    print("Cantidad de aves muertas por región: ", "\n" )
#    print("Nombre de la región", region, ": ",cantidad, "\n")

"""

# 1. Leer el archivo y almacenar los datos en una lista
#archivo_aves = open('aves.txt', 'r')
#lineas = archivo_aves.readlines()
#archivo_aves.close()

# 2. Crear una función que filtre los datos para enero 2023
def funcion_b(datos):
    total_muertes = 0
    
    for lista in datos:
    #columnas = lista.strip().split(',')
        fecha = lista[0]
        total_muertes_ave = int(lista[7])
        
        dia, mes, year = fecha.split('-')
        
        if mes == '01' and year == '2023':
            total_muertes += total_muertes_ave

    return total_muertes




"""
def funcion_b(datos):
    nombre_archivo = open('aves.txt', 'r')
    total_aves_muertas_enero_2023 = 0
    for linea in nombre_archivo:
        campos = linea.strip().split(',')
        fecha = campos[0]
        total_muertes = int(campos[7])
        dia, mes, anio = fecha.split('-')
        if mes == '01' and anio == '2023':
            total_aves_muertas_enero_2023 += total_muertes
    nombre_archivo.close()

    #print("Total de aves muertas en enero de 2023:", total_aves_muertas_enero_2023)
    
#def funcion_c(datos):
#def funcion_d(datos):
#def funcion_e(datos):
"""
def funcion_muerte_aves(datos):
    especies_e = {'Gaviota garuma' : 0, 
                  'Piquero' : 0,
                  'Gaviota Frankin' : 0,
                  'Pelícano' : 0,
                  'Guanay' : 0}
    for lista in datos:
        dat = lista.strip().split(',')
        especie = dat[6].strip()
        total_muertes = int(dat[7].strip())
        if especie in especies_e:
            especies_e[especie] += total_muertes
    return especies_e

def graficar_e(especies_e):
    especies = list(especies_e.keys())
    muertes = list(especies_e.values())

    plt.figure(figsize=(10, 6))
    plt.bar(especies, muertes, color=['blue', 'green', 'red', 'cyan', 'magenta'])
    plt.xlabel('Especie')
    plt.ylabel('Cantidad de Muertes')
    plt.title('Cantidad de Muertes por Especies Solcitadas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Ruta al archivo aves.txt

#def funcion_piquero(datos):
#def funcion_franklin(datos):
#def funcion_pelicano(datos):
#def funcion_guanay(datos):

"""
def genera_salida(b):

def genera_salida(b, promedios, minimo, maximo):
    sal = open('resultados.txt', 'w')
    for promedio in promedios:
        sal.write('Promedio '+ str(promedio[0]) + ' : ' + str(promedio[1]) + '\n\n')
    fecha = maximo[0].split('-')
    sal.write('El mayor valor corresponde al dia '+fecha[0]+ ' del mes '+fecha[1]+' de '+fecha[2]+'\n\n')
    fecha = minimo[0].split('-')
    sal.write('El menor valor corresponde al dia '+fecha[0]+ ' del mes '+fecha[1]+' de '+fecha[2]+'\n\n')
    sal.close()
    
    print("Casos de aves muertas mes Enero del año 2023: ",b, "\n")
 
"""
    #def muestra_datos(sismo_mayor, sismos_7_8, sismos_8_9, sismos_9, sismo_16, sismo_17, sismo_18, sismo_19, sismo_20, sismo_21):
    #print("Fecha:", sismo_mayor[0],"y hora:", sismo_mayor[1],"del mayor sismo registrado\n")
    #print("Cantidad de sismos >= 7.0 y < 8.0:",sismos_7_8,"\n")


#def grafica(y):
 #   x = [Gaviota_Garuma, Piquero, Gaviota_Franklin, Pelicano, Guanay]
  #  plt.bar(x, y)
   # plt.show()

if __name__ == '__main__':
    datos = lectura_datos('aves.txt') 
    #datos = 'aves.txt'
    #muestra_regiones = lista_regiones(datos)
    #print ("Listado de regiones: ", muestra_regiones)
    #a = funcion_a(datos)
    #print("Cantidad de aves muertas por región: ", a)
    b = funcion_b(datos)
    print("Casos aves muertas mes enero del año 2023: ", b)
    #c = funcion_c(datos)
    #d = funcion_d(datos)
    #e = funcion_e(datos)
    #gaviota_garuma = funcion_garuma(datos)
    #piquero = funcion_piquero(datos)
    #gaviota_franklin = funcion_franklin(datos)
    #pelicano = funcion_pelicano(datos)
    #guanay = funcion_guanay(datos)
    #genera_salida(b)
    #grafica([gaviota_garuma, piquero, gaviota_franklin, pelicano, guanay]) 
    especies_e = funcion_muerte_aves(datos)
    funcion_muerte_aves(especies_e)

"""
  ent = open('wnosetxt.txt')
sal = open('nuevo.txt', 'w')
for linea in ent:
    sal.write(linea)
ent.close()
sal.close()
"""
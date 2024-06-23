#Autores = ["Julio Díaz Garcia", "-", "Simón Pichuante Olguín"]
import matplotlib.pyplot as plt
from datetime import datetime

def lectura_archivo(archivo):
    ent = open(archivo)
    datos = []
    for linea in ent:
        linea = linea.rstrip('\n')
        lista = linea.split(',')
        datos.append(lista)
    ent.close()
    return datos


def cantidad_aves_muertas_region(archivo):
    regiones = {}
    for dato in archivo:
        #Detectar si la región de la línea ya esta en un contador
        if dato[2] not in regiones:
            regiones[dato[2]] = 0 #Si la región no se encuentra se agrega un contador
        regiones[dato[2]] += int(dato[7]) #Añadir muertes al contador
    return regiones
    

def cantidad_aves_muertas_enero2023(archivo):
    cantidad = 0 #Iniciar contador
    for dato in archivo: #Recorrer los datos
        #Se usa librería estándar de Python para las fechas
        fecha = datetime.strptime(dato[0], "%d-%m-%Y") #Objeto fecha str
        if fecha.year == 2023 and fecha.month == 1:
            cantidad += int(dato[7]) #Añadir muertes si corresponden a la fecha filtrada
    return cantidad
    

def cantidad_tagua_cartagena(archivo):
    cantidad = 0 #Iniciar contador
    for dato in archivo: # recorremos los datos
        # si coincide los criterios de búsqueda agregamos las muertes
        if dato[6] == "Tagua - (Fulica armillata)" and dato[3] == "Cartagena":
            cantidad += int(dato[7])
    return cantidad


def cantidad_piquero_12_febrero2023(archivo):
    cantidad = 0 #Iniciar contador
    for dato in archivo: #Recorrer los datos
        if dato[0] == "12-02-2023" and dato[6] == "Piquero - (Sula variegata)":
            cantidad += int(dato[7]) 
    return cantidad


def imprimir_datos(a, b, c, d):
    salida = open("resultado.txt", "w")
    salida.write("Autores Julio Díaz García - Simón Pichuante Olguín\n")
    salida.write("Cantidad de aves muertas por región: \n")
    for regiones in a.keys():
        salida.write("\t"+regiones+": "+str(a[regiones])+"\n")
    salida.write("Casos aves muertas mes enero del año 2023: "+str(b)+"\n")
    salida.write("En la comuna de Cartagena se detectaron "+str(c)+" Taguas muertas.\n")
    salida.write("Las muertes detectadas para el 12 de febrero del 2023 de la especie Piquero son: "+str(d)+"\n")
    salida.close()

def grafico_aves(archivo):
     #Se crea un diccionario con contadores de las aves que agregaremos al gráfico final
    especies = {"Gaviota Garuma" : 0,
            "Piquero" : 0,
            "Gaviota de Franklin" : 0,
            "Pelicano" : 0,
            "Guanay" : 0
            }
    
    for dato in archivo:
        if dato[6] == "Gaviota garuma - (Larus modestus)":
            especies["Gaviota Garuma"] += int(dato[7])
        if dato[6] == "Piquero - (Sula variegata)":
            especies["Piquero"] += int(dato[7])
        if dato[6] == "Gaviota de Franklin - (Larus pipixcan)":
            especies["Gaviota de Franklin"] += int(dato[7])
        if dato[6] == "Pelicano - (Pelecanus thagus)":
            especies["Pelicano"] += int(dato[7])
        if dato[6] == "Guanay - (Phalacrocorax bougainvillii)":
            especies["Guanay"] += int(dato[7])
    #Se suma en contadores según especie de ave 

    ax = plt.subplot()
    ax.bar(especies.keys(), especies.values())

    for etiqueta in ax.get_xticklabels():
        etiqueta.set_rotation(10)

    plt.show()
    return 1


if __name__ == '__main__':
    archivo = lectura_archivo('aves.txt')
    muertes_region = cantidad_aves_muertas_region(archivo)
    muertes_enero2023 = cantidad_aves_muertas_enero2023(archivo)
    tagua_cartagena = cantidad_tagua_cartagena(archivo)
    piquero_12febrero2023 = cantidad_piquero_12_febrero2023(archivo)
    grafico = grafico_aves(archivo)
    imprimir_datos(muertes_region, muertes_enero2023, tagua_cartagena, piquero_12febrero2023)


elementos = []

def lectura():
    archivo = open("Cancion.txt","r")
    linea = archivo.readline()
    while linea !="":
        eliminar = linea.replace("\n","")
        separar = eliminar.split()
        elementos.append(separar)
        print (linea)
        linea = archivo.readline()
    archivo.close()

def contador():
    contador = 0
    for i in range(0,len(elementos)):
        for j in range (0,len(elementos[i])):
            contador = contador+1
    print ("\nTiene: ",contador,"palabras") 
##contador()
lectura()
contador()


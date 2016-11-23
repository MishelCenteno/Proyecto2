
def contador():
    archivo = open("Cancion.txt","r")
    linea = archivo.readline()
    contador = 0
    while linea != "":
        contador = contador+1
        linea = archivo.readline()
    archivo.close()
    print("Numero de lineas: "contador)

contador()

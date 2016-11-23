
def contador():
    archivo = open("Cancion.txt","r")
    linea = archivo.readline()
    contador = 0
    while linea != "":
        contador = contador+1
        linea = archi.readline()
    archivo.close()
    print(contador)

contador()

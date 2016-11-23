def creartxt():
    archivo=open('practica.txt','w')
    archivo.close()
    
def grabartxt():
    archi =open("practica.txt","a")
    archi.write("Mishel Centeno")
    archi.write("Josue Cando")
    archi.write("Programacion Avanzada")
    archi.close()
def leertxt():
    archivo=open('practica.txt','r')
    linea=archivo.readline()
    while linea!="":
        print (linea)
        linea=archivo.readline()
    archivo.close()

creartxt()
grabartxt()
leertxt()

def creartxt():
    archivo=open('practica.txt','w')
    archivo.close()
    
def grabartxt():
    archi =open("practica.txt","a")
    archi.write("Mishel Centeno\n")
    archi.write("Josue Cando\n")
    archi.write("Programacion Avanzada\n")
    archi.close()
    
def leertxt():
    archivo=open('practica.txt','r')
    linea=archivo.readline()
    while linea!="":
        print (linea)
        linea=archivo.readline()
    archivo.close()
    
def leertxtenlista():
    archivo=open('practica.txt','r')
    lineas=archivo.readlines()
    print(lineas)
    archivo.close()
creartxt()
grabartxt()
leertxt()
leertxtenlista()

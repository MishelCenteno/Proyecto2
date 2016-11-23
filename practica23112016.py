def creartxt():
    archivo=open('practica.txt','w')
    archivo.close()
    
def grabartxt():
    archi =open("practica.txt","a")
    archi.write("Mishel Centeno")
    archi.write("Josue Cando")
    archi.write("Programacion Avanzada")
    archi.close()

creartxt()
grabartxt()

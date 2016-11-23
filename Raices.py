def factorar1(a,b,c):
    x1 = (-b + ((b**2)-(4*a*c))**(1/2))/(2*a)
    x2 = (-b - ((b**2)-(4*a*c))**(1/2))/(2*a)
    return x1, x2

def archivo(texto):
    archi = open("resultado.txt","w")
    archi.close()
    archi = open("resultado.txt","a")
    archi.write(texto)
    archi.close()
    archi = open("resultado.txt","r")
    linea = archi.readlines()
    print(linea)
    archi.close()
    
def main():
    a = int(input("a: "))
    if a > 0:
        b = int(input("b: "))
        c = int(input("c: "))
        discriminante  = ((b**2)-(4*a*c))**1/2
        if discriminante >= 0:
            resultado = factorar1(a,b,c)
            archivo(str(resultado))
        else:
            print("No existen raices negativas \n\nIngrese de nuevo:")
            main()
    else:
        print("Tiene que ser mayor a cero \n\nIngrese de nuevo")
        main()
main()


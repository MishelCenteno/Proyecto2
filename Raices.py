def factorar1(a,b,c):
    x1 = (-b + ((b**2)-(4*a*c))**(1/2))/(2*a)
    return x1
def archivo(texto):
    archivo = open("resultado.txt")
    archivo.write(texto)
    lineas = archivo.readlines()

def main():
    a = int(input("a: "))
    if a > 0:
        b = int(input("b: "))
        c = int(input("c: "))
        discriminante  = ((b**2)-(4*a*c))**1/2
        if discriminante >= 0:
            resultado = factorar1(a,b,c)
            print(resultado)
        else:
            print("No existen raices negativas \n\nIngrese de nuevo:")
            main()
    else:
        print("Tiene que ser mayor a cero \n\nIngrese de nuevo")
        main()
main()


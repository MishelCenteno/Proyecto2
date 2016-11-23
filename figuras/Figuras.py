## EPN-ESFOT-ASI Programacion Avanzada

## 20112016.py
## Versión: 2.0
## Calculo del area y el perimetro de una figura

## Autor: Jhosue Obaco y Mishel Centeno
## Fecha: 22-Nov-2016

import sys
def perimetro(num_lad,long_lad):
    perimetro = num_lad*long_lad
    return perimetro
##esta funcion solo contendra la longitud del tamaño
def area(long_lad):
    lado_c = round(long_lad,2)
    lado_b = round(long_lad/2,2)
    expo_c = round(lado_c**2,2)
    expo_b = round(lado_b**2,2)
    resta  =  round(expo_c - expo_b,2)
    altura = round(resta**(1/2),5)
    area = round(long_lad*altura/2,2)
    return area

def menu():
    try:
        num_lad = int(input("Número de lados: "))
        if num_lad >= 3 and num_lad <=10:
            long_lad = float(input("Longitud de un lado: "))
            if num_lad == 3:
                print("La figura es un triangulo")
                area_fig = area(long_lad)
                perimetro_fig = perimetro(num_lad,long_lad)
                
            elif num_lad == 4:
                print("La figura es un cuadrado")
                area_fig = long_lad**2
                perimetro_fig = perimetro(num_lad,long_lad)
            elif num_lad == 5:
                print("La figura es un pentagono")
                area_fig = num_lad*area(long_lad)
                perimetro_fig = perimetro(num_lad,long_lad)

            elif num_lad == 6:
                print("La figura es un hexagono")
                area_fig = num_lad*area(long_lad)
                perimetro_fig = perimetro(num_lad,long_lad)
            elif num_lad == 7:
                print("La figura es un hectagono")
                area_fig = num_lad*area(long_lad)
                perimetro_fig = perimetro(num_lad,long_lad)
            elif num_lad == 8:
                print("La figura es un octagono")
                area_fig = num_lad*area(long_lad)
                perimetro_fig = perimetro(num_lad,long_lad)
            elif num_lad == 9:
                print("La figura es un nonagono")
                area_fig = num_lad*area(long_lad)
                perimetro_fig = perimetro(num_lad,long_lad)
            elif num_lad == 10:
                print("La figura es un decagono")
                area_fig = num_lad*area(long_lad)
                perimetro_fig = perimetro(num_lad,long_lad)
            print("El Area de la figura es:",area_fig," y el perimetro es: ",perimetro_fig)
            repetir()
            menu()
        else:
            print("No existe figura \n")
            menu()
    except ValueError:
        print("Dato incorrecto \n\nIngrese de nuevo")
        menu()
        
def repetir():
    op=0;
    while(op!="s"):
        print("Desea continuar, presion si o no para finalizar")
        op=input("si/no:")
        if (op=="si"):## si la opcion es si  se repite el menu  donde seleciona  nuevamente la lista
            menu()
        else:    
            print ("Adios")##si  desea salir se cierra el programa
            sys.exit()
    

def main():
    print("Programa Para Calcular el Area Y perimetro")
    menu()
    
main()


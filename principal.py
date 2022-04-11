def planteamiento():
    print("*"*90)
    print(" "*35,"EL JUNQUILLO CHINO"," "*35)
    print("*"*90)
    print("Un granjero chino se encontraba mirando un lago circular del cual salía exactamente en el")
    print("centro una porción de un junquillo, este junquillo nacía exactamente en el centro del")
    print("fondo del lago, el granjero observó que cuando el viento soplaba el junquillo se inclinaba") 
    print("sin deformarse y al tocar la orilla del lago quedaba exactamente cubierto por el agua.") 
    
    print("*"*90)
    print(" "*41,"OUTPUT"," "*41)
    print("*"*90)
    print("¿Cuál es la profundidad del lago en metros?")

    print("*"*90)
    print(" "*41,"INPUT"," "*41)
    print("*"*90)
    print("Ingrese un par de enteros separados por un espacio en donde:")
    print(" 1. El primer entero corresponde a un número entre 1 y 10.000 que representa el diámetro")
    print("    del lago en metros")
    print(" 2. El segundo entero corresponde a un número entre 1 y 1.000 que representa la porción") 
    print("    visible del junquillo en centímetros")
    print("")
    print("Tenga en cuenta lo siguiente:")
    print(" 1. Pueden ingresar tantos pares de números como desee")
    print(" 2. Si escribe cero en los dos enteros, el programa comenzara a realizar el cálculo de la") 
    print("    profundidad para cada par de enteros ingresados") 
    print("*"*90)

def solucion():
    tabla = "Diámetro del lago(m) \t Porción visible del junquillo(m) \t Profundidad del lago(m)"
    salida = ""

    while True:
        enteros = input("Ingrese el diámetro del lago y la porción visible del junquillo: ")
        split = enteros.split(" ")
        
        if len(split) == 2:
            try:
                i = int(split[0])
                j = int(split[1])/100

                if not(i == 0 and j == 0):
                    if not((i < 0 or j < 0) or (i > 10000 or j*100 > 1000)):
                        solucion = (-j/2) + ((i**2)/(8*j))
                        salida = salida + str(i) + "\t\t\t " + str(j) + "\t\t\t\t\t " + str(round(solucion, 1)) + "\n"
                    else:
                        print("Los valores ingresados no son validos")
                else:
                    print("*"*90)
                    break
            except ValueError:
                print("Los valores ingresados no son validos")              
            
        else:
            print("Los valores ingresados no son validos")
            
    print("La profundidad del lago para cada par de enteros ingresado es: ")
    print(tabla)
    print(salida)

planteamiento()
solucion()
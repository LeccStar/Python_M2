#Longitud de una frase
print("Revisemos si una palabra tiene cierta longitud.")

#Primero se solicita al usuario ingresar la palabra y se le comentan las características necesarias:
word = input("Ingrese una palabra de entre 4 y 8 letras: ")

#Posteriormente utilizamos las estructuras de control (if, elif)
# en conjunto con operadores de compraración para determinar si la palabra es correcta.
if len(word) >= 4 and len(word) <= 8:
    print("La palabra es correcta.")
elif len(word) < 4:
    print(f"Hacen falta letras. Solo tiene {len(word)} letras.")
elif len(word) > 8:
    print(f"Sobran letras. Tiene {len(word)} letras.")


#Encuentra el cuadrante
print("Ahora revisemos si podemos identificar en qué cuadrante se encuentran unas coordenadas en el plano cartesiano (Sin ingresar el 0).")

#Con la estructura try except podemos cerciorarnos que el usuario solo ingrese numeros
# y en caso de no ser así, arrojarle un mensaje apropiado.
try:
    x = int(input("Ingrese X: "))
    y = int(input("Ingrese Y: "))

except:
    print("Debe ingresar números:")
    exit()

#Despues utilizamos operadores de comparación para revisar todas las formas de coordenadas posibles 
# y entregar una respuesta dependiendo del resutado.
if x == 0 or y == 0:
    print("Ninguna coordenada puede ser 0.")
    exit()
if x>0 and y>0:
    print ('El punto se encuentra en el Cuadrante I')
if x<0 and y>0:
    print ('El punto se encuentra en el Cuadrante II')
if x<0 and y<0:
    print ('El punto se encuentra en el Cuadrante III')
if x>0 and y<0:
    print ('El punto se encuentra en el Cuadrante VI')
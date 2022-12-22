try:
    currentYear = int(input("Ingrese el año actual: "))
    yearToCalc = int(input("Ingrese otro año para calcular: "))
    
except:
    print("Error: Ingrese solo numeros")
    exit()

diff = currentYear - yearToCalc

if (diff < 0):
    diff = abs(diff)
    print( f'Aún faltan {diff} años para el año {yearToCalc}')

elif(diff == 0):
    print ('¡Es el mismo año!')

else:
    print(f'Han pasado {diff} años desde el año {yearToCalc}')

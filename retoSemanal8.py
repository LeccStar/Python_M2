english_colors = {
    "rojo": "red",
    "naranja": "orange",
    "amarillo": "yellow",
    "verde": "green",
    "azul": "blue",
    "violet": "purple"
}
german_colors = {
    "rojo": "rot",
    "naranja": "orange",
    "amarillo": "gelb",
    "verde": "grün",
    "azul": "blau",
    "violet": "violett"
}
response = ""

print("Bienvenid@, esta aplicación te permite traducir al inglés o al alemán los colores que ingreses.")
option = input("¿Quieres el color en ingles (I) o en alemán (A)? ")

if option != "I" and option != "i" and option != "A" and option != "a":
    print("Se ha ingresado una opcion no válida")
    exit()

color = input("Ingresa uno de los colores del arcoiris en español: ")
color = color.lower()
newColor = color.split()

for color in newColor:
    if (option == "i" or option == "I") and color in english_colors:
        response = response +"< "+ english_colors[color] + " >"
    elif (option == "a" or option == "A") and color in german_colors:
        response = response +"< "+ german_colors[color] + " >"
    else:
        response = response + color + " "
print(response)
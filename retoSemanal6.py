password = input("Ingrese una contraseña que inicie con un número: ")

if (password[0].isnumeric()):
    for i in range(3):
        repeticion = input("Vuelva a ingresar su contraseña: ")
        if password == repeticion:
            print('Contraseña correcta')
            break
        else: 
            print("Las contraseñas no coinciden")
            continue
    if password != repeticion:
        print("Numero de intentos máximo alcanzado")

else:
    print('La contraseña debe empezar con un número')



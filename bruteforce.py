import time

mayusculas = "QWERTYUIOPASDFGHJKLZXCVBNM"
minusculas = "qwertyuiopasdfghjklzxcvbnm"
numeros = "1234567890"
simbolos = "~!@#$%^&*`"

alfabeto = mayusculas + minusculas + numeros + simbolos

contrasena = input("Ingresa una contraseña: ")

longitud = int(input("Ingresa la longitud a probar: "))



indices = [0] * longitud

intentos = 0
inicio = time.time()

while True:

    intento = ""
    for i in indices:
        intento += alfabeto[i]

    print(intento)
    intentos += 1


    if intento == contrasena:
        break

    posicion = longitud - 1

    while posicion >= 0:
        indices[posicion] += 1

        if indices[posicion] < len(alfabeto):
            break
        else:
            indices[posicion] = 0
            posicion -= 1

    if posicion < 0:
        break  

fin = time.time()

print("\n====== RESULTADOS ======")
print("Contraseña encontrada:", intento)
print("Intentos realizados:", intentos)
print("Tiempo total:", round(fin - inicio, 4), "segundos")

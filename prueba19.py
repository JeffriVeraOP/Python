import time
contador = 1
# Escribe un bucle for que cuente hasta cinco.
for conteo in range(1,6):
    # Cuerpo del bucle: imprime el número de iteración del bucle y la palabra "Mississippi".
    print(contador, "Mississippi")
    time.sleep(1)
    # Cuerpo del bucle, emplea : time.sleep(1)
    contador += 1
# Escribe una función print con el mensaje final.
print("Lista o no, aquí vengo")
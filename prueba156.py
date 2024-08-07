school_class = {}

while True:
    name = input("Ingresa el nombre del estudiante: ")
    if name == '':
        break
    
    score = int(input("Ingresa la calificación del estudiante (0-10): "))
    if score not in range(0, 11):
        break
    
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)
        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)

''' Explicacion linea por linea
línea 1: crea un diccionario vacío para ingresar los datos; el nombre del alumno es empleado como clave, mientras que todas las calificaciones asociadas son almacenadas en una tupla (la tupla puede ser el valor de un diccionario, esto no es un problema)
línea 3: se ingresa a un bucle "infinito" (no te preocupes, saldrémos de el en el momento indicado)
línea 4: se lee el nombre del alumno aquí;
línea 5-6: si el nombre es una cadena vacía (), salimos del bucle;
línea 8: se pide la calificación del estudiante (un valor entero en el rango del 0-10)
línea 9-10: si la puntuación ingresada no está dentro del rango de 0 a 10, se abandona el bucle;
línea 12-13: si el nombre del estudiante ya se encuentra en el diccionario, se alarga la tupla asociada con la nueva calificación (observa el operador +=)
línea 14-15: si el estudiante es nuevo (desconocido para el diccionario), se crea una entrada nueva, su valor es una tupla de un solo elemento la cual contiene la calificación ingresada;
línea 17: se itera a través de los nombres ordenados de los estudiantes;
línea 18-19: inicializa los datos necesarios para calcular el promedio (sum y counter).
línea 20-22: se itera a través de la tupla, tomado todas las calificaciones subsecuentes y actualizando la suma junto con el contador.
línea 23: se calcula e imprime el promedio del alumno junto con su nombre.
'''

#Como seguramente sabrás, debido a algunas razones astronómicas, el año puede ser bisiesto o común. Los primeros tienen una duración de 366 días, mientras que los últimos tienen una duración de 365 días.
'''Desde la introducción del calendario Gregoriano (en 1582), se utiliza la siguiente regla para determinar el tipo de año:
si el número del año no es divisible entre cuatro, es un año común.
de lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
de lo contrario, si el número del año no es divisible entre 400, es un año común.
de lo contrario, es un año bisiesto.
Observa el código en el editor - solo lee un número de año y debe completarse con las instrucciones que implementan la prueba que acabamos de describir.
El código debe mostrar uno de los dos mensajes posibles, que son Año Bisiesto o Año Común, según el valor ingresado.
Sería bueno verificar si el año ingresado cae en la era Gregoriana y emitir una advertencia de lo contrario: No dentro del período del calendario Gregoriano. Consejo: utiliza los operadores != y %.'''

year = int(input("Ingrese el año: "))

if year >= 1582:
    print("El año ", year, " está dentro del periodo gregoriano")
    if (year % 4) != 0:
        print ("El año ", year, " es un año común")
    elif (year % 100) != 0:
        print("El año ", year, " es un año bisiesto")
    elif (year % 400) != 0:
        print ("El año ", year, " es un año común")
    else:
        print("El año ", year, " es un año bisiesto")
else:
    print("El año ", year, " no está dentro del periodo gregoriano")
'''Tu tarea es escribir y probar una función que toma un argumento (un año) y devuelve True si el año es un año bisiesto, o False si no lo es.
La semilla de la función ya se muestra en el código esqueleto del editor.
Nota: también hemos preparado un breve código de prueba, que puedes utilizar para probar tu función.
El código utiliza dos listas - una con los datos de prueba y la otra con los resultados esperados. El código te dirá si alguno de tus resultados no es válido.'''

'''si el número del año no es divisible entre cuatro, es un año común.
de lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
de lo contrario, si el número del año no es divisible entre 400, es un año común.
de lo contrario, es un año bisiesto.'''
    
def is_year_leap(yr):
    if yr % 4 != 0:
        return False
    elif yr % 100 != 0:
        return True
    elif yr % 400 != 0:
        return False
    else:
        return True
    
#

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")
'''Tu tarea es escribir un programa que elimine todas las repeticiones de números de la lista. El objetivo es tener una lista en la que todos los números aparezcan no más de una vez.Sugerencia: Te recomendamos que crees una nueva lista como área de trabajo temporal - no necesitas actualizar la lista actual.'''

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
clean_list = []
for i in my_list:
    if i not in clean_list:
        clean_list.append(i)
        
print("La lista con elementos únicos:")
print(clean_list)
'''Tu programa debe:

pedir al usuario que ingrese una palabra.
utilizar user_word = user_word.upper() para convertir la palabra ingresada por el usuario a mayúsculas; hablaremos sobre los llamados métodos de cadena y el upper() muy pronto, no te preocupes.
emplea la ejecución condicional y la instrucción continue para "devorar" las siguientes vocales A , E , I , O , U de la palabra ingresada.
asigna las letras no consumidas a la variable word_without_vowels e imprime la variable en la pantalla.
Analiza el código en el editor. Hemos creado word_without_vowels y le hemos asignado una cadena vacía. Utiliza la operación de concatenación para pedirle a Python que combine las letras seleccionadas en una cadena más larga durante los siguientes giros de bucle, y asignarlo a la variable word_without_vowels'''

word_without_vowels = ""
# Indicar al usuario que ingrese una palabra
# y asignarla a la variable user_word.
user_word = str(input("Ingrese una palabra: "))
user_word = user_word.upper()

for letter in user_word:
    # Completa el cuerpo del bucle.
    if letter == "A":
        continue
    elif letter == "E":
        continue 
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        word_without_vowels = word_without_vowels + letter
# Imprimir la palabra asignada a word_without_vowels.
print(word_without_vowels)

#También existe un método denominado values(), funciona de manera muy similar al de keys(), pero regresa una lista de valores. Este es un ejemplo sencillo:

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

for french in dictionary.values():
    print(french)

# Como el diccionario no es capaz de automáticamente encontrar la clave de un valor dado, el rol de este método es algo limitado.

secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

user_number = int(input("Hola asqueroso muggle, atrevete a adivinar el número secreto: "))

while user_number != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    user_number = int(input("Asqueroso muggle, sigue intentando adivinar el número secreto: "))

print("¡Bien hecho, muggle! Eres libre ahora.")
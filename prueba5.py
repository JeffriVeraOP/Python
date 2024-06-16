n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
n3 = int(input("Ingrese el tercer numero: "))

upn = n1

if n2 > upn:
    upn = n2

if n3 > upn:
    upn = n3

print("El mayor número es: ", upn)
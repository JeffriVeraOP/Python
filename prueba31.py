'''Toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0;
si es par, evalúa un nuevo c0 como c0 ÷ 2;
de lo contrario, si es impar, evalúe un nuevo  c0  como 3 × c0 + 1;
si c0 ≠ 1, salta al punto 2.'''

c0 = int(input("Ingrese un numero entero positivo y diferente de 0: "))
counter = 0
while c0 > 0:
    if c0 % 2 == 0:
        c0 = c0 // 2
        print(c0)
        counter += 1
        if c0 == 1:
            break
    elif c0 % 2 != 0:
        c0 = int((3 * c0) + 1)
        print(c0)
        counter += 1
        if c0 == 1:
            break
print("Pasos: ", counter)
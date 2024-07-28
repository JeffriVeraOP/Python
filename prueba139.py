def factorial(n):
    return n * factorial(n - 1)


print(factorial(4))

'''La función no tiene una condición de terminación, por lo tanto Python arrojara una excepción (RecursionError: maximum recursion depth exceeded)'''
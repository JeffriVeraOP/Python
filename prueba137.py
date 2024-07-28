def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

# Probando la función
for i in range(1, 10):
    print(f"fib({i}) = {fib(i)}")
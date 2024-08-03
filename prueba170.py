def f(x):
    if x == 0:
        return 0
    return x + f(x - 1)


print(f(3))

# 3 + f(2)= 2 + f(1) = 1 + f(0) = 0
# 6

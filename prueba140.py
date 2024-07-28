def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)
    #(25 + fun(28) = 28 + fun(31) = 3) = 56


print(fun(25))



def is_a_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

'''def is_a_triangle(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    return False

print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))'''
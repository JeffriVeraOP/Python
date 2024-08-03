dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dictionary['one']

for k in range(len(dictionary)):
    v = dictionary[v]

# v = two
# 1º iteracion == v = three
# 2º iteracion == v = one
# 3º iteracion == v = one

print(v)

# two


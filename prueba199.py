dct = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dct['three'] # 'one'

for k in range(len(dct)):
    v = dct[v] # two, three, one

print(v)


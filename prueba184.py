my_list = [1, 2]

for v in range(2):
    my_list.insert(-1, my_list[v])

print(my_list)

# [1, 1, 1, 2]
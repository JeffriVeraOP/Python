lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0

for number in lst:
    add += number
    #0+1 = 1 1+2 = 3 3+3 = 6 6+4 = 10 10+5 = 15
    lst_2.append(add)
    # lst_2 = [1, 3, 6, 10, 15]

print(lst_2)


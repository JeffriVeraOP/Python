my_list =  [x * x for x in range(5)]

# 0, 1, 4, 9, 16

def fun(lst):
    del lst[lst[2]]
    return lst

print(fun(my_list))
# my_list = [0, 1, 4, 9]

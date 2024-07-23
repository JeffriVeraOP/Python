list_1 = ["A", "B", "C"]
list_2 = list_1
# list_2 = ["A", "B", "C"]
list_3 = list_2
# list_3 = ["A", "B", "C"]
del list_1[0]
# list_1 = ["B", "C"]
del list_2[:]
# list_2 = []
print(list_3)
# list_3 = []


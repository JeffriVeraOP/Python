lst = [[x for x in range(3)] for y in range(3)]
# lst = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
for r in range(3): # 0, 1, 2
    for c in range(3): # 0, 1, 2
        if lst[r][c] % 2 != 0: 
            print("#") # -- ###


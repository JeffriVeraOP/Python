blocks = int(input("Ingresa el número de bloques: "))
height = 0
blocks_n = 1
while blocks >= blocks_n:
    height += 1
    blocks = blocks - height
    blocks_n += 1
    
print("La altura de la pirámide:", height)

print('\n'*10)

ground = "M"*31
print('STAR'.center(31))
print('BUCKS'.center(31))
counter = 1
for n in range(1,10,1):
    print(("*"*n).center(31),counter,'--------','n =',n)
    counter = counter+1
for n in range(3):
    print('|'.center(31))
print(ground)

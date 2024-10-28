import random

table1 = [

]

num = 5


for i in range(num):
    table1.append([])
    for j in range(num):
        table1[i].append(random.randint(0,2)//2)

for i in table1:
    print(i)

def szomszade(x, y):
    ilands = []
    if x > 0:
        if table1[x-1][y] == 1:
            ilands.append([x-1, y])
    if y > 0:
        if table1[x][y-1] == 1:
            ilands.append([x, y-1])

    if x < (num-1):
        if table1[x+1][y] == 1:
            ilands.append([x+1, y])

    if y < (num - 1):
        if table1[x][y+1] == 1:
            ilands.append([x, y+1])

    table1[x][y] = 0
    for i in ilands:
        szomszade(i[0], i[1])
        
sziget = 0

for x in range(num):
    for y in range(num):
        if table1[x][y] == 1:
            sziget+=1
            szomszade(x, y)

print(sziget)




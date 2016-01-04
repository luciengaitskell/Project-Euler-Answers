totalSum=0

for ii in range(1,1000):
    if ii % 3 == 0 or ii % 5 == 0:
        totalSum=totalSum+ii
print(totalSum)
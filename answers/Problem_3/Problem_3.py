num=600851475143
#num=10
ii=num-1
primes = []

# primes
while ii > 1:
    jj=ii-1
    flag=False
    while jj>1:
        flag=True
        if ii % jj == 0:
            flag=False
            break
        jj= jj-1
    if flag == True:
        primes.append(ii)
        print primes
    ii= ii-1

print primes


# OTHER

'''
while ii > 1:
    if num % ii == 0:
        jj=ii
        flag=False
        while jj>1:
            flag=True
            if ii % jj == 0:
                flag=False
                break
            jj= jj-1
        if flag == True:
            print ii
            break
    ii= ii-1
    #print(ii)

print ii
'''
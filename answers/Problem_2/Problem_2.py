firstNum=1
secondNum=2
newNum=0
totalSum=0
while True:
    if secondNum % 2 == 0:
        totalSum+=secondNum
    
    newNum=firstNum+secondNum
    firstNum=secondNum
    secondNum=newNum
    if newNum > 4000000:
        break
print totalSum
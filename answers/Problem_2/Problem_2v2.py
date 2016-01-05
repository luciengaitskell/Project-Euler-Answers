firstNum=0
secondNum=1
newNum=0
totalSum=0
while True:
    newNum=firstNum+secondNum
    firstNum=secondNum
    secondNum=newNum
    
    if secondNum > 4000000:
        break
    if secondNum % 2 == 0:
        totalSum+=secondNum
    
    
print totalSum
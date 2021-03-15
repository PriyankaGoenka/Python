def showNumbers(limit):
    for i in range(0,limit+1):
        if i%2==0:
            print(i,"EVEN")
            
        elif i%2!=0:
            print(i,"ODD")
        else:
            pass

n=int(input("Enter the value of limit: "))
print(showNumbers(n))
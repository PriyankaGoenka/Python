n=int(input("Enter the value of n: "))
x=filter(lambda x:x%3!=0 and x%7==0,range(1,n+1))
print(list(x))
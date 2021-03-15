x=(1,2,3,4,5,6,7,8,9,10)
x=list(x) #convert tuple to list
y=[] #initialize an empty list
for i in x:
    if i%2==0:
        y.append(i)
print(tuple(y))

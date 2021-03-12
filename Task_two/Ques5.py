
x=int(2000)
y=int(3200)
for i in range(x-1,y+1):
    if i%7==0 and i%5!=0:
        print(i)
import math

num=input("Input some comma seperated numbers: ")
num=num.split(',')
a=[]
for D in num:
    Q=math.sqrt((2*50*int(D)/30))
    a.append(Q)
print("New list is: ",a)

s= input("Enter the alphanumeric string: ")
s=list(s)
l=[]
for i in s:
    if i.isalpha():
        l.append(i)
#print(l)

d={} 

for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

print("Occurance of each letter in the string:"+ str(d))
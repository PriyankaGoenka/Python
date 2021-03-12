s=input("Enter the string: ")
d={}
for keys in s:
    d[keys]=d.get(keys,0)+1
print(d)
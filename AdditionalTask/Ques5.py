s=input("Enter the string: ")
r=s[::-1]
#index=r.index
for i in r:
    if i=='a' or i=='e' or i=='i'or i=='o' or i=='u':
        index=s.index(i)
        print(i, index)

        
       
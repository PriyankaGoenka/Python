def case(s):
    U=0
    L=0
    for i in s:
        if i.isupper()==True:
            U+=1
        elif i.islower()==True:
            L+=1
        else:
            pass
    #return U,L
    print("No. of Uppercase characters:", U, "No of Lower case characters:",L)
   
    

s=input("Enter the string: ")
x=case(s)
print(x)
#print("No. of Uppercase characters: ", U, "No of Lower case characters: ",L)

 

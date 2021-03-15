def square():
    l=[]                    #Create an empty list
    for i in range(1,21):
        i=i**2              #Square of numbers
        l.append(i)
    return(tuple(l))        #Convert list to tuples

print(square())
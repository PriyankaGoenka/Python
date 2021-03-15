
def unique(L): # L stands for list
    New=[]   #Initialize empty list
    L=set(L) #Convert list to set, set removes duplicate elements
    for i in L:
        New.append(i)
    return New

M=[1,1,1,2,2,3,3,4,4,5,5,7,7,8,8]
print(unique(M))


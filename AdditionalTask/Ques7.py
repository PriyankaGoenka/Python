x=[1,2,3,4,5,6,7,8,9,-1]
for i in x:
    for j in x[1:]:
        if i+j==8:
            print(i,j)
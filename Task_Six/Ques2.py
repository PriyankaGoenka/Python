stu=['Nilay','Priyanka','Jyoti','Navin']
sub=['Maths','Science','Commerce','Business']
d=dict(zip(stu,sub)) #using zip function
print(d)
di={stu[i]:sub[i] for i in range(len(stu))} #using for loop
print(di)

even_list=[]
odd_list=[]

n = input('Enter elements of a list in the range(0,50) separated by space: ')
print("\n")
user_list = n.split()
print('list: ', user_list)

for k in user_list:
    k = int(k)

    if k%2==0:
       even_list.append(k)
       print(even_list[:5])
    elif k%2!=0:
       odd_list.append(k)
       print(odd_list[:5])
    else:
       pass


s1=0
for i in even_list:
    s1=s1+i
print("Sum of even list:",s1)
print("Maximum value in even list is:", max(even_list))


s2=0
for i in odd_list:
    s2=s2+i
print("Sum of odd list:",s2)
print("Maximum value in odd list is:", max(odd_list))



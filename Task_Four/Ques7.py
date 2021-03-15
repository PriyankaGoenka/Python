def func(s1,s2):
    if len(s1)>len(s2):
        return s1
    elif len(s2)>len(s1):
        return s2
    elif len(s1)==len(s2):
        return (s1+ '\n' + s2)
    else:
        pass

str1=input("Enter first string: ")
str2=input("Enter second string: ")
print(func(str1,str2))
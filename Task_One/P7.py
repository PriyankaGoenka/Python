

x= "Hello my name is Priyanka"
# UPPER CASE
print(x.upper())
y= x.split()
print(y)

'''for i in y:
    if i.isalnum():
        i.capitalize()
        z=''.join(i)
        print(z)'''
# Pascal case or upper camel case
z= ''.join(i.capitalize() for i in y if i.isalnum())
print(z)

# lower camel case
w= z[0].lower()+z[1:]
print(w)

# Snake case
T= x.lower()
M= T.split()
print(M)

X= '_'.join(M)
print(X)




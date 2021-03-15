n=input("Enter the string: ")  #Enter the string with hyphen
l=n.split('-')                 # Split the alphabets and hyphen
print(l)                       # Print alphabets
l.sort()                       # Sort these alphabets 
print("-".join(l))             # Join alphabets with hyphen 
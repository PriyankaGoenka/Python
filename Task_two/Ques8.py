str= input("Enter the string: ")
letter=0
digit=0
for i in str:
    if i.isalpha():
        letter+=1
    elif i.isdigit():
        digit+=1
print("Number of digits: ", digit)
print("Number of letters: ",letter)

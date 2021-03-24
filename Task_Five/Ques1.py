#while True:
try:
   i=input("Enter the value: ")
   x= i**2
   print(x)

except SyntaxError as error:
    print("Syntax Error! Try again!")
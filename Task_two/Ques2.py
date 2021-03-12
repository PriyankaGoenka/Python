
print("Note: At a time user can only perform one action")
print("Enter your choice: ")
print("1: Addition")
print("2: Subtraction")
print("3: Multiplication")
print("4: Division")
print("5: Average")

choice=eval(input("Enter your choice: "))
num1=eval(input("Enter the first number: "))
num2=eval(input("Enter the second number: "))


while True:
    if choice==1:
        ans= num1+num2
        print("ans:", + ans)
        if ans<0:
            print("Negative")
        break
    
    elif choice==2:
        ans= num1-num2
        print("ans:",+ ans)
        if ans<0:
            print("Negative")
        break

    elif choice==3:
        ans= num1*num2
        print("ans:", + ans)
        if ans<0:
            print("Negative")
        break

    elif choice==4:
        ans= num1/num2
        print("ans:", + ans)
        if ans<0:
            print("Negative")
        break

    elif choice==5:
        num3=eval(input("Enter the third number: "))
        num4=eval(input("Enter the fourth number: "))
        ans= (num1+num2+num3+num4)/4
        print("ans:", + ans)
        if ans<0:
            print("Negative")
        break
    
    else:
        print("Enter the correct option")
        break



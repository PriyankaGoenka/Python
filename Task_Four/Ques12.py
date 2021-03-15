def func():
    n=5
    y=int(input("Enter the value of y: "))
    try:
        x=n/y
        return x
    except:
        print("Error dividing by zero")


print(func())
try:
    x=input("Enter digits:")
    if len(x)>4:
        raise Exception("The length is too long/short!!! Please provide only four digits.")
except Exception as e:
    print(e)
else:
    print("Entered digits are of correct length")



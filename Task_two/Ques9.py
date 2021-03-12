Lucky_number=7
#number=int(input("Guess the lucky number: "))
while True:
    number=int(input("Guess the lucky number: "))
    if number==Lucky_number:
        print("Guess is correct!")
        break
    else:
        print("Your guess is wrong!")
    answer=input("Do you want to guess again: " )
    if answer=="no":
        break
    elif answer=="yes":
        continue

    

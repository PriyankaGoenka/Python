Lucky_number=7
counter=0
while counter<=5:
    number=int(input("Guess the lucky number: "))
    if number==Lucky_number:
        print("Good guess!")
    else:
        print("Try again!")
    counter=counter+1
    if counter==5:
        print("Game over!")
        break

   

    
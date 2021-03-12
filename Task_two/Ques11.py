Lucky_number=7
counter=0
while counter<=5:
    number=int(input("Guess the lucky number: "))
    if number==Lucky_number:
        print("Good guess!")
        break
    elif counter<4:
        print("Try again!")
    counter=counter+1
    if counter==5 and number!=Lucky_number:
        print("Sorry but that was not very successful")
        break
    

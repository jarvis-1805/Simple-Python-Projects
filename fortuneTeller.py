print("\n\t\t\t\tThe Fortune Teller!")
print("You will select a color and a numer and I will tell you what your future holds for you!!!")
c = input("\nDo you want to play the game!!! ('y' or 'n'): ")

while c == 'y':
    color = input("\nChoose a color from - Yellow, Green, Blue, Red: ")
    
    if color == 'Yellow' or color == 'yellow' or color == 'YELLOW' or color == 'Green' or color == 'green' or color == 'GREEN':
        
        while True:
        
            number = int(input("Select a number from - 1, 2, 5, 6: "))
        
            if number == 1:
                print("\nWorried about your future! Don't worry! You'll 100% get what you want! Be patient!")
                break
            elif number == 2:
                print("\nYou will become a millionaire at the ae of 35!")
                break
            elif number == 5:
                print("\nYou will have a great family with 10 kids!")
                break
            elif number == 6:
                print("\nYou will become famous and everyone will love you!")
                break
            else:
                print("Numbers - 1, 2, 5, 6 are the only numbers allowed!")
        
    elif color == 'Blue' or color == 'blue' or color == 'BLUE' or color == 'Red' or color == 'red' or color == 'RED':
        
        while True:
        
            number = int(input("Select a number from - 3, 4, 7, 8: "))
        
            if number == 3:
                print("\nYou will a happy life for 100 years at least!")
                break
            elif number == 4:
                print("\nYou will become a successful doctor one day!")
                break
            elif number == 7:
                print("\nAll your dreams will come true, just be patient!")
                break
            elif number == 8:
                print("\nYou're lucky! You'll have it all one day!")
                break
            else:
                print("Numbers - 3, 4, 7, 8 are the only numbers allowed!")
        
    else:
        print("Colors - Yellow, Green, Blue, Red are only colors allowed!")
        continue
    
    c = input("\nDo you want to play again? ('y' or 'n'): ")
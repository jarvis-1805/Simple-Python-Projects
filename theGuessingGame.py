import random

print("\t\t\tThe Guessing Game!")
print("WARNING!!! Once you enter the game you have to guess the right number!!!\n")
c = input("Still want to enter the game!!! ('y' or 'n'): ")
print()

while c == 'y':
    
    true_value = random.randint(1, 100)
    
    while True:
    
        chosed_value = int(input("Choose a number between 1 and 100: "))
       
        if (chosed_value == true_value):
            print("\nYou guessed it right!!! Good job!!!")
            break
       
        elif (chosed_value > 100 or chosed_value < 0):
            print("\nYou did not choose the number within range!!!")
       
        elif (chosed_value < true_value):
            print("\nYour number is low...Try again!!!")
       
        elif (chosed_value > true_value):
            print("\nYour number is high...Try again!!!")
   
    c = input("\nDo you want to play again? ('y' or 'n'): ")

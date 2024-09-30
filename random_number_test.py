from random import randrange

'''
Generate a random number from a range of 0 to 10
To adjust the range edit the values within the parentheses ()
The first number controls the lower bounds and the second controls the higher bounds
'''
#initializing variables
random_number = randrange(0, 100)
counter = 1
print("Try to guess the random number between 0 to 10 in 10 tries!")
choice = "y"
#creating loop that runs the game
while choice == "y" or "Y":
    guess = int(input(f"Guess #{counter}. Enter your next guess: "))
    while True:
        if counter > 9:
            break
        if guess == random_number:
            counter += 1
            break
        elif guess != random_number:
            counter += 1
            if guess > random_number:
                print("You guessed incorrectly. Your guess was higher than the number, please try again")
            else:
                print("You guessed incorrectly. Your guess was lower than the number, please try again")
            print()
            guess = int(input(f"Guess #{counter}. Enter your next guess: "))
     #setting win and loss conditions   
    if counter > 9 and guess != random_number:
        print(f"You have no more guesses. The number was: {random_number}")
    elif guess == random_number:
        if counter == 2:
            print(f"You guessed correctly! It took you {counter} try")
        else:
            print(f"You guessed correctly! It took you {counter - 1} tries.")
    counter = 1
    random_number = randrange(0, 10)
    #giving choice to player to play again or end program
    while True:
        choice = input("Do you want to play again (y/n)?: ")
        if choice.lower() == "y":
            choice = "y"    
            break
        elif choice.lower() == "n":
            print("Thanks for playing!")
            print()
            print("Completed by, Cade Armstrong")
            choice = "n"
            break
        elif choice.lower() != "y" or "n":
            choice = input("Please input either y or n: ")
            if choice.lower == "n":
                print("Thanks for playing!")
                print()
                print("Completed by, Cade Armstrong")
                choice = "n"
        break
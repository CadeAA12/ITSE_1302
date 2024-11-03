from random import randrange


def get_weapon():
    print("SELECT YOUR WEAPON")
    print("\n1.Rock \n2.Paper \n3.Scissors")
    weapon = int(input("ENTER YOUR CHOICE: "))
    return weapon

def opponent_weapon():
    opposing_weapon = randrange(1,4)
    return opposing_weapon


def determine_winner():
    weapon = get_weapon()
    opposing_weapon = opponent_weapon()
    if weapon == opposing_weapon:
        print("It's a tie!")
    elif weapon == 1:
        if opposing_weapon == 2:
            print("Paper beats rock, you lose!")
        else:
            print("Rock beat scissors, you win!")
    elif weapon == 2:
        if opposing_weapon == 1:
            print("Paper beats rock, you win!")
        else:
            print("Scissors beats paper, you lose!")
    elif weapon == 3:
        if opposing_weapon == 1:
            print("Rock beats scissors, you lose!")
        else:
            print("Scissors beats paper, you win!")

def main():
    choice = "y"
    while choice.lower() == "y":
        determine_winner()
        choice = input("Would you like to play again? (y/n): ")
        if choice.lower() == "n":
            print("Completed by,  Cade Armstrong")
        elif choice.lower() != "y" or "n":
            print("You must input either y or n")
            choice = input("Would you like to play again? (y/n): ")


if __name__ == "__main__":
    main()
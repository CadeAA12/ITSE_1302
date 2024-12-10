def main():
    print("The String Replacement Tool")
    print("================================")

    main_string = get_input("Enter the main string: ")
    substring = get_input("Enter the substring to search for: ")

    index = get_substring(main_string, substring)

    if index != -1:
        replace = choice_input("Do you want to replace this substring? ")
        if replace.lower() == "y":
            new_substring = get_input("Enter the new substring: ")
            new_main = main_string.replace(substring, new_substring)
            print(f"The new string is: {new_main}")
        else:
            print("No changes were made")
    print("================================")
    print("Thank you for using this program!")
    print("Completed by, Cade Armstrong")

def get_input(prompt):
    return input(prompt)

def get_substring(main_string, substring):
    index = main_string.find(substring)
    if index != -1:
        print(f"{substring} was found at index {index}")
        print("================================")
    else:
        print("The substring was not found")
    return index

def choice_input(prompt):
    while True:
        choice = input(prompt)
        if choice.lower() == "y" or choice.lower() == "n":
            return choice
        print("Invalid response. Please try again.")

if __name__ == "__main__":
    main()
import random

grade_list = []

def main():
    choice = -2
    while choice == -2:
        choice_2 = int(input("Please input your grade or -1 to stop: "))
        if choice_2 == -1:
            break
        else:
            grade_list.append(choice_2)
        
        
    print(grade_list)

    print("Removing lowest grade...")
    minimum = min(grade_list)
    min_grade = grade_list.index(minimum)
    del_grade = grade_list.pop(min_grade)
    print(grade_list)

    print("Removing random grade...")
    random_grade = random.choice(grade_list)
    remove_grade = grade_list.remove(random_grade)
    print(grade_list)

    print("Edit a grade")
    for i, item in enumerate(grade_list, start=1):
        print(f"{i}. {item}")
    edit_grade = int(input("Enter a grade to edit: "))
    if edit_grade > i:
        edit_grade = int(input("Enter a valid grade: "))
    else:
        new_grade = int(input("Enter the new grade: "))
        grade_list[edit_grade - 1] = new_grade
        print(grade_list)
    
    print("Sorting and reversing list...")
    grade_list.sort()
    grade_list.reverse()
    print(grade_list)

    print("Obtaining grade total and average...")
    total = sum(grade_list)
    print(f"Total: {total}")
    average = total / len(grade_list)
    print(f"Average: {round(average)}")

    print("Completed by, Cade Armstrong")

if __name__ == "__main__":
    main()
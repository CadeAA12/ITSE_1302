def main():
    student_information = {}
    students = {
        "Steve":
            {'ID': '1', 'GPA': '3.2', 'Credits Completed': '46.0', 'Grades': [90, 88, 95]},
        "Tony":
            {'ID': '2', 'GPA': '2.8', 'Credits Completed': '70.0', 'Grades': [78, 84, 90]}
    }
    print(students)
    
    
    print("Listing Students...")
    for key in students.keys():
        print(key)
    
    
    print("Accessing student information...")
    print("Student\tID\tGPA\tCredits Completed\tGrades")
    for key, value in students.items():
        print(key)

        for inner_value in value:
            print(f"{value[inner_value]}")

    
    print("Removing a student...")
    students.pop("Steve")
    print(students)

    print("Accessing GPA...")
    for i in students:
        print(students.get("Tony").get('GPA'))

    print("Clearing registry...")
    students.clear()
    print(students)

    print("Completed by, Cade Armstrong")

              
if __name__=="__main__":
    main()
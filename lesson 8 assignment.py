import csv



def create_file(file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Phone', 'Email'])
    print("File created successfully")

def add_contact(file_name):
    name = input("Enter contact name: ")
    email = input("Enter contact email: ")
    phone = input("Enter contact phone: ")
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])
    

def read_contacts(file_name):
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Name: {row[0]} Phone: {row[1]} Email: {row[2]}")
    

def edit_contact(file_name):
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        contacts = list(reader)
            
        
    print("\nExisting Contacts:")
    for index, contact in enumerate(contacts, 1):
        print(f"{index}. Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}")

        
    contact_index = int(input("\nEnter the number of the contact you want to edit: ")) - 1
    if contact_index < 0 or contact_index >= len(contacts):
        print("Invalid contact number. Please try again.")
        

    contact_to_edit = contacts[contact_index]
    print(f"Editing contact: {contact_to_edit[0]}")
    new_phone = input("Enter new phone number: ")
    new_email = input("Enter new email address: ")

    
    contact_to_edit[1] = new_phone
    contact_to_edit[2] = new_email

            
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file) 
        writer.writerows(contacts)  
            
    print("Contact updated successfully.")
    

def main():
    file_name = "contacts.csv"
    print("Contact Manger App")
    while True:
        print("Enter the number that corresponds with the action\n1.Create new contact file\n2.Add new contact\n3.List all contacts\n4.Edit a contact\n5.Exit")
        choice = input("Enter your selection:")
        if choice == '1':
            create_file(file_name)
        elif choice == '2':
            add_contact(file_name)
        elif choice == '3':
            read_contacts(file_name)
        elif choice == '4':
            edit_contact(file_name)
        elif choice == '5':
            print("Exiting program")
            print("Completed by, Cade Armstrong")
            break
        else:
            print("Invalid option. Try again")

if __name__ == "__main__":
    main()
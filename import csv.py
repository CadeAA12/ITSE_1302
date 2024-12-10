import csv

# Define the function to create a new contact CSV file
def create_contact_csv(file_name):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write header row
        writer.writerow(['Name', 'Phone', 'Email'])
    print("Contact CSV file created successfully.")

# Define the function to add a new contact to the CSV file
def add_contact(file_name):
    name = input("Enter the name of the contact: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        # Append the new contact data
        writer.writerow([name, phone, email])
    print("Contact added successfully.")

# Define the function to view all contacts
def view_contacts(file_name):
    try:
        with open(file_name, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            print("\nContacts List:")
            for row in reader:
                print(f"Name: {row[0]}, Phone: {row[1]}, Email: {row[2]}")
    except FileNotFoundError:
        print("The contact file does not exist. Please create a file first.")

# Define the function to modify an existing contact
def edit_contact(file_name):
    try:
        with open(file_name, mode='r') as file:
            reader = csv.reader(file)
            contacts = list(reader)
            
        # Skip the header row
        header = contacts[0]
        contact_list = contacts[1:]
        
        if not contact_list:
            print("No contacts available to edit.")
            return
        
        print("\nExisting Contacts:")
        for index, contact in enumerate(contact_list, 1):
            print(f"{index}. Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}")

        try:
            contact_index = int(input("\nEnter the number of the contact you want to edit: ")) - 1
            if contact_index < 0 or contact_index >= len(contact_list):
                print("Invalid contact number. Please try again.")
                return

            contact_to_edit = contact_list[contact_index]
            print(f"Editing contact: {contact_to_edit[0]}")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email address: ")

            # Update the contact information
            contact_to_edit[1] = new_phone
            contact_to_edit[2] = new_email

            # Re-write the file with updated information
            with open(file_name, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(header)  # Write the header row
                writer.writerows(contact_list)  # Write the updated contact list
            
            print("Contact updated successfully.")
        except ValueError:
            print("Invalid input. Please try again.")

    except FileNotFoundError:
        print("The contact file does not exist. Please create a file first.")

# Main function to run the program
def main():
    file_name = "contacts.csv"

    while True:
        print("\n===== Contact Management System =====")
        print("1. Create a new contact CSV file")
        print("2. Add a new contact")
        print("3. View all contacts")
        print("4. Edit a contact")
        print("5. Exit")
        
        choice = input("Please choose an option (1-5): ")

        if choice == '1':
            create_contact_csv(file_name)
        elif choice == '2':
            add_contact(file_name)
        elif choice == '3':
            view_contacts(file_name)
        elif choice == '4':
            edit_contact(file_name)
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Call the main function to run the program
if __name__ == "__main__":
    main()

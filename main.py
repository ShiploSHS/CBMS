from contact_manager import add_contact, view_contacts, remove_contact, search_contact
from file_manager import load_contacts, save_contacts


def main():
    contacts = load_contacts('contacts.csv')  # Load existing contacts from file
    if contacts is None:
        contacts = []
    filename = 'contacts.csv'  # Specify the file where contacts will be saved

    while True:
        # Show menu
        print("\n*****Shiplo's Contact Manager*****\n")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Remove Contact")
        print("4. Search Contact")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_contact(contacts, filename)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            remove_contact(contacts, filename)
        elif choice == "4":
            search_contact(contacts)
        elif choice == "0":
            save_contacts(contacts, filename)
            print("Thanks for using Shiplo's Contact Manager")
            break
        else:
            print("Invalid choice! Please try again.")


# Call the main function to start the program
if __name__ == "__main__":
    main()

from contact import Contact
from file_manager import save_contacts


# Function to add a new contact
def add_contact(contacts, filename):
    print("Add a new contact:")

    while True:
        name = input("Enter name: ").strip()
        if name:  # Ensure name is not empty
            break
        else:
            print("Name cannot be empty. Please try again.")

    while True:
        phone_number = input("Enter phone number: ").strip()
        if phone_number.isdigit() and len(phone_number) > 0:
            if not any(contact.phone_number == phone_number for contact in contacts):
                break
            else:
                print("This phone number already exists. Please enter a different one.")
        else:
            print("Invalid phone number.")

    while True:
        email = input("Enter email: ").strip()
        if '@' in email and '.' in email:
            break
        else:
            print("Invalid email format. Please try again.")

    address = input("Enter address: ").strip()

    contact = Contact(name, phone_number, email, address)
    contacts.append(contact)
    save_contacts(contacts, filename)
    print(f"Contact '{name}' added successfully!")


# Function to view all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print("\nContacts:")
    for contact in contacts:
        print(contact)


# Function to remove a contact by phone number
def remove_contact(contacts, filename):
    phone_number = input("Enter phone number to remove: ").strip()
    contact_to_remove = None
    for contact in contacts:
        if contact.phone_number == phone_number:
            contact_to_remove = contact
            break

    if contact_to_remove:
        contacts.remove(contact_to_remove)
        save_contacts(contacts, filename)
        print(f"Contact with phone number {phone_number} has been removed.")
    else:
        print("Contact not found.")


# Function to search for a contact by name or phone number
def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ").strip()
    found_contacts = [contact for contact in contacts if
                      search_term in contact.name or search_term in contact.phone_number]

    if found_contacts:
        print("\nSearch Results:")
        for contact in found_contacts:
            print(contact)
    else:
        print("No matching contacts found.")

import csv
from contact import Contact

def load_contacts(filename):
    contacts = []
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if 'name' in row and 'phone_number' in row and 'email' in row and 'address' in row:
                    contact = Contact(row['name'], row['phone_number'], row['email'], row['address'])
                    contacts.append(contact)
                else:
                    print(f"Skipping invalid row: {row}")
    except FileNotFoundError:
        print("No contacts file found. Starting fresh.")
    return contacts

def save_contacts(contacts, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write header row
        writer.writerow(['name', 'phone_number', 'email', 'address'])
        # Write contact data
        for contact in contacts:
            writer.writerow([contact.name, contact.phone_number, contact.email, contact.address])

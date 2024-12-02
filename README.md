# Contact Book Management System

A Python-based Command Line Interface (CLI) application to manage a contact book. This project demonstrates core Python programming concepts such as file handling, object-oriented programming (OOP), and modular design. The program supports adding, viewing, searching, and removing contacts while persisting data across sessions using a CSV file.

---

## Features

- **Add Contacts**: Create new contacts with details like name, phone number, email, and address.
  - Ensures unique phone numbers.
  - Supports special characters in names.
- **View Contacts**: Displays all saved contacts in a user-friendly tabular format.
- **Search Contacts**: Find contacts by name, phone number, or email.
- **Remove Contacts**: Delete a contact by specifying its name or other details.
- **Save and Load**: Automatically saves contacts to a CSV file and loads them on startup.
- **Input Validation**: Handles invalid inputs gracefully with meaningful error messages.

---

## Technologies Used

- **Language**: Python (no external libraries required).
- **Modules**:
  - `csv`: For file handling.
  - `os`: For file management (optional in some cases).

---

## File Structure
-📂 Project Directory:
-├── main.py             # Entry point; CLI menu and program flow.
-├── contact.py          # Defines the Contact class.
-├── contact_manager.py  # Core contact operations (add, view, remove, search).
-├── file_manager.py     # Handles file I/O for loading and saving contacts.
-└── contacts.csv        # Storage file for contact data.

---

## How to Run

1. Clone this repository to your local machine:
   ```bash
   git clone <repository-url>
   cd <repository-folder>

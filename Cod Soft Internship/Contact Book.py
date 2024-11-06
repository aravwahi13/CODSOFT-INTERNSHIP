contacts = {}


def add_contact():
    name = input("Enter name: ").title()
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts[name] = {"phone": phone, "email": email, "address": address}
    print(f"Contact '{name}' added successfully.")


def view_contacts():
    if contacts:
        print("\nContact List:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}")
    else:
        print("No contacts found.")


def search_contact():
    search_term = input("Enter name or phone number to search: ").title()
    found = False
    for name, info in contacts.items():
        if search_term in name or search_term in info['phone']:
            print(f"\nName: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
            found = True
    if not found:
        print("Contact not found.")


def update_contact():
    name = input("Enter the name of the contact to update: ").title()
    if name in contacts:
        print(
            f"Current Details - Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}, Address: {contacts[name]['address']}")
        phone = input("Enter new phone number (or press Enter to keep current): ")
        email = input("Enter new email (or press Enter to keep current): ")
        address = input("Enter new address (or press Enter to keep current): ")

        # Update only if the user provided a new value
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        if address:
            contacts[name]['address'] = address

        print(f"Contact '{name}' updated successfully.")
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter the name of the contact to delete: ").title()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print("Contact not found.")


def main():
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

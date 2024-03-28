try:
    class Contact:
        def __init__(self, name, number, email):
            self.name = name
            self.number = number
            self.email = email

    class ContactBook:
        def __init__(self):
            self.contacts = []

        def add_contact(self, contact):
            self.contacts.append(contact)
            print("Contact added successfully.")

        def view_contacts(self):
            if not self.contacts:
                print("No contacts available.")
            else:
                print("Contact List:")
                for i, contact in enumerate(self.contacts):
                    print(f"{i + 1}. Name: {contact.name}, Phone: {contact.number}")

        def search_contact(self, search_name):
            results = []
            for contact in self.contacts:
                if search_name.lower() in contact.name.lower() or search_name in contact.number:
                    results.append(contact)
            if results:
                print("Search Results:")
                for contact in results:
                    print(f"Name: {contact.name}, Phone: {contact.number}, Email: {contact.email}")
            else:
                print("No matching contacts found.")

        def update_contact(self, search_name, new_contact):
            for contact in self.contacts:
                if search_name.lower() in contact.name.lower() or search_name in contact.number:
                    contact.name = new_contact.name
                    contact.number = new_contact.number
                    contact.email = new_contact.email
                    print("Contact updated successfully.")
                    return
            print("Contact not found.")

        def delete_contact(self, search_name):
            for i, contact in enumerate(self.contacts):
                if search_name.lower() in contact.name.lower() or search_name in contact.number:
                    del self.contacts[i]
                    print("Contact deleted successfully.")
                    return
            print("Contact not found.")

    def menu():
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

    def main():
        contact_book = ContactBook()
        while True:
            menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter name: ")
                number = input("Enter phone number: ")
                email = input("Enter email: ")
                contact = Contact(name, number, email)
                contact_book.add_contact(contact)

            elif choice == "2":
                contact_book.view_contacts()

            elif choice == "3":
                search_name = input("Enter name or phone number to search: ")
                contact_book.search_contact(search_name)

            elif choice == "4":
                search_name = input("Enter name or phone number of contact to update: ")
                new_name = input("Enter new name: ")
                new_number = input("Enter new phone number: ")
                new_email = input("Enter new email: ")
                new_contact = Contact(new_name, new_number, new_email)
                contact_book.update_contact(search_name, new_contact)

            elif choice == "5":
                search_name = input("Enter name or phone number of contact to delete: ")
                contact_book.delete_contact(search_name)

            elif choice == "6":
                print("Exiting Contact Book.....")
                break

            else:
                print("Invalid choice. Please try again.")

    if __name__ == "__main__":
        main()
except:
    "Error, please try again later!!!"
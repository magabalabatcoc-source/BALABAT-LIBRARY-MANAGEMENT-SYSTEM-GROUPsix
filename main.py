def show_books(library):
    print("\nLibrary Inventory")
    print("-" * 60)

    total_books = total_available = total_borrowed = 0

    for book, info in library.items():
        available = info['available']
        total = info['total']
        borrowed = total - available

        borrowers_list = ", ".join(f"{n} ({q})" for n, q in info['borrowers'].items()) or "None"

        print(f"{book}")
        print(f"  Total: {total} | Available: {available} | Borrowed: {borrowed}")
        print(f"  Borrowers: {borrowers_list}")
        print("-" * 60)

        total_books += total
        total_available += available
        total_borrowed += borrowed

    print(f"Total books: {total_books}")
    print(f"Available: {total_available}")
    print(f"Borrowed: {total_borrowed}")
    print("-" * 60)


def borrow_book(library):
    name = input("Enter your name: ").strip()
    book_input = input("Enter the title of the book you want to borrow: ").strip()

    # Case-insensitive match
    book = next((b for b in library if b.lower() == book_input.lower()), None)
    if not book:
        print("Book not found.")
        return

    info = library[book]

    if info['available'] <= 0:
        print(f"Sorry, all copies of '{book}' are borrowed.")
        return

    try:
        qty = int(input(f"How many copies of '{book}' do you want to borrow? "))
        if qty <= 0:
            print("Please enter a positive number.")
        elif qty > info['available']:
            print(f"Only {info['available']} copies are available.")
        else:
            info['available'] -= qty
            info['borrowers'][name] = info['borrowers'].get(name, 0) + qty
            print(f"{name}, you borrowed {qty} copies of '{book}'.")
    except ValueError:
        print("Invalid number.")


def return_book(library):
    name = input("Enter your name: ").strip()
    book_input = input("Enter the title of the book you want to return: ").strip()

    book = next((b for b in library if b.lower() == book_input.lower()), None)
    if not book:
        print("Book not found.")
        return

    info = library[book]

    if name not in info['borrowers']:
        print(f"{name}, you didn't borrow '{book}'.")
        return

    borrowed_qty = info['borrowers'][name]
    print(f"You borrowed {borrowed_qty} copies of '{book}'.")

    try:
        qty = int(input("How many copies do you want to return? "))
        if qty <= 0:
            print("Enter a positive number.")
        elif qty > borrowed_qty:
            print("You cannot return more than you borrowed.")
        else:
            info['available'] += qty

            if qty == borrowed_qty:
                del info['borrowers'][name]
            else:
                info['borrowers'][name] -= qty

            print(f"Thank you, {name}, for returning {qty} copies.")
    except ValueError:
        print("Invalid number.")


def main():
    library = {
        "Harry Potter": {"total": 25, "available": 25, "borrowers": {}},
        "The Hobbit": {"total": 25, "available": 25, "borrowers": {}},
        "1984": {"total": 25, "available": 25, "borrowers": {}},
        "To Kill a Mockingbird": {"total": 25, "available": 25, "borrowers": {}},
        "The Great Gatsby": {"total": 25, "available": 25, "borrowers": {}}
    }

    print("Welcome to the Library Management System")

    while True:
        print("\nMain Menu:")
        print("1. Show Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            show_books(library)

        elif choice == "2":
            borrow_book(library)

        elif choice == "3":
            return_book(library)

        elif choice == "4":
            confirm = input("Are you sure you want to exit? (yes/no): ").strip().lower()
            if confirm == "yes":
                print("Thank you for using the Library Management System. Goodbye!")
                break
            else:
                print("Returning to menu...")

        else:
            print("Invalid choice.")



if __name__ == "__main__":
    main()

   


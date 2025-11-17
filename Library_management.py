class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}

    def add_book(self, book, quantity):
        if book in self.books:
            self.books[book] += quantity
        else:
            self.books[book] = quantity

    def display_books(self):
        print("Available Books:")
        for book, quantity in self.books.items():
            print(f"{book} - {quantity}")

    def lend_book(self, book):
        if book in self.books and self.books[book] > 0:
            self.books[book] -= 1
            print(f"You have borrowed '{book}'. Please return it within due time.")
        else:
            print("Sorry, this book is not available right now.")

    def return_book(self, book):
        if book in self.books:
            self.books[book] += 1
            print(f"Thank you for returning '{book}'.")
        else:
            print("Invalid book name. Please check and try again.")


def main():
    library = Library("My Library")

    while True:
        print("\nMenu:")
        print("1. Add a book")
        print("2. Display available books")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            book_name = input("Enter the name of the book: ")
            quantity = int(input("Enter the quantity: "))
            library.add_book(book_name, quantity)
            print("Book added successfully!")

        elif choice == '2':
            library.display_books()

        elif choice == '3':
            book_name = input("Enter the name of the book you want to borrow: ")
            library.lend_book(book_name)

        elif choice == '4':
            book_name = input("Enter the name of the book you want to return: ")
            library.return_book(book_name)

        elif choice == '5':
            print("Thank you for using the library management system. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__== "__main__":
    main()
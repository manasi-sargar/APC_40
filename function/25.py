books = {
    "Python": True,
    "Java": True,
    "C++": True
}
def add_book(name):
    books[name] = True
def issue_book(name):
    if name in books and books[name]:
        books[name] = False
        print("Book issued")
    else:
        print("Book not available")
def return_book(name):
    books[name] = True
def search_book(name):
    if name in books:
        print("Book found")
    else:
        print("Book not found")
def display_books():
    for book, available in books.items():
        if available:
            print(book)
display_books()
issue_book("Python")
display_books()
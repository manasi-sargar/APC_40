books = ["Python", "C++", "Java"]

# Add a book
books.append("HTML")

# Search a book
if "Python" in books:
    print("Python book is available")
else:
    print("Python book is not available")

# Remove a book
books.remove("C++")

# Display books
print("All books:", books)

# Count books
print("Total books:", len(books))
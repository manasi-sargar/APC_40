books = ["Python", "C++", "Java"]
books.append("HTML")
if "Python" in books:
    print("Python book is available")
else:
    print("Python book is not available")
books.remove("C++")
print("All books:", books)
print("Total books:", len(books))
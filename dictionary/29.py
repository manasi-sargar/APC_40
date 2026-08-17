books={101:"Python Basics",102:"Data Science",103:"Machine Learning"}
books[104]="Java Programming"
id=int(input("Enter book ID to search: "))
if id in books:
    print("Book:",books[id])
else:
    print("Book not found")
del books[102]
print("All books:",books)
print("Total books:",len(books))
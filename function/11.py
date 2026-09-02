#11.	Write a function that accepts a string and returns its reverse.
def reverse_string(text):
    return text[::-1]
text=input("enter string: ")
print("reverse: ",reverse_string(text))
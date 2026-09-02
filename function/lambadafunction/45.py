words = ["apple", "banana", "cat", "elephant", "dog"]
result = list(filter(lambda x: len(x) > 5, words))
print(result)
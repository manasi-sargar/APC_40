words = ["apple", "banana", "cat", "elephant", "dog"]
lengths = list(map(lambda x: len(x), words))
print("Lengths:", lengths)
long_words = list(filter(lambda x: len(x) > 5, words))
print("Long words:", long_words)
sorted_words = sorted(words, key=lambda x: len(x))
print("Sorted:", sorted_words)
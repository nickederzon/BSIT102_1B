word = input("Enter a word: ")
word_length = len(word)
numbers = []

for i in range(word_length):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

print(numbers)

average = sum(numbers) / len(numbers)

print(f"The length of the word is {word_length}")
print(f"The average of the numbers is {average}")

if word_length < average:
    print(f"The length of the word '{word}' is less than the average.")
elif word_length > average:
    print(f"The length of the word '{word}' is greater than the average.")
else:
    print(f"The length of the word '{word}' is equal to the average.")
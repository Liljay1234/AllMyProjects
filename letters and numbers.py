
letters = input("please gime me a word")

print (letters)

numbers = []
for letter in letters:
  number = ord(letter) - 96
  numbers.append(number)

print(numbers)
Sum=sum(numbers)
print(Sum)

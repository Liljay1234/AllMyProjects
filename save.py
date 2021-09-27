#give a word to be turned into a lettersum
letters = input("please gime me a word")

print (letters)
#list to save the numbers of each character
numbers = []
#code to separate the inputted words characters to turn them into numbers
for letter in letters:
  number = ord(letter) - 96
  numbers.append(number)
#adds the sum of all the character numbers together
print(numbers)
Sum=sum(numbers)
print(Sum)

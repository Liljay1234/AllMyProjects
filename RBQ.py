import os
from collections import Counter

a_file = open(r"C:\Users\joshw\PycharmProjects\pythonProject\Files for python\pythonnumbertext.txt", "r")

list_of_lists = []
for line in a_file:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  list_of_lists.append(line_list)

a_file.close()


print(len(list_of_lists))

counter = (0)
popnumber = (0)
all_Sums = []
all_words = []
all_numbers = []
odd_number = []
odd_words = []
#
inputnum = int(input("plese put in a number"))
numbers = []
while counter < 172823:
    Sum = (0)
    word = list_of_lists.pop(popnumber)
    sentence = ''.join(map(str, word))
    for letter2 in sentence:
      number2 = ord(letter2) - 96
      numbers.append(number2)
    counter = counter + 1
    Sum=sum(numbers)
    numbers.clear()
    if Sum == inputnum:
      all_words.append(sentence)
      all_numbers.append(Sum)
    if Sum % 2 != 0:
        odd_number.append(Sum)
        odd_words.append(sentence)
    all_Sums.append(Sum)
else:
    print(all_numbers, all_words)
    print("that is all the words")
    print(len(odd_number))
    common_element = Counter(all_Sums)
    print(common_element.most_common(2))
print("done")








import os
from collections import Counter
#this opens a file full of words
a_file = open(r"C:\Users\joshw\PycharmProjects\pythonProject\Files for python\pythonnumbertext.txt", "r")

#this creates a list then adds all the words from the file into the list and then closes the file
list_of_lists = []
for line in a_file:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  list_of_lists.append(line_list)
a_file.close()

#printed length of list to help with while loop counter value later
print(len(list_of_lists))

#all lists and variables needed to complete all the questions
counter = (0)
popnumber = (0)
all_Sums = []
all_words = []
all_numbers = []
odd_number = []
odd_words = []
numbers = []
#You input a number which is used to find all the words that equal to its value
inputnum = int(input("plese put in a number"))
#this loop is to keep running till all words have been checked
while counter < 172823:
    #sum resets in order to stop errors
    Sum = (0)
    #this pops a word from the list and turns splits it letters into separate characters
    word = list_of_lists.pop(popnumber)
    sentence = ''.join(map(str, word))
    #turns the characters in the numbers with a=1 to z=26
    for letter2 in sentence:
      number2 = ord(letter2) - 96
      numbers.append(number2)
    #counter gets added to stop the while loop at the correct time
    counter = counter + 1
    #adds the sum of the characters from the word that was popped of the list then clears to be added in the next calculation
    Sum=sum(numbers)
    numbers.clear()
    #adds all the words that equal the number you inputed at the start into a list to display later
    if Sum == inputnum:
      all_words.append(sentence)
      all_numbers.append(Sum)
    #counts how many odd numbers are in the original file with all the words
    if Sum % 2 != 0:
        odd_number.append(Sum)
        odd_words.append(sentence)
    #counts all the sums of all words into a list
    all_Sums.append(Sum)
else:
    #prints the answers to your input aswell as all odd numbers
    print(all_numbers, all_words)
    print("that is all the words")
    print(len(odd_number))
    #tells you what the most common lettersum is in the word file
    common_element = Counter(all_Sums)
    print(common_element.most_common(2))
print("done")

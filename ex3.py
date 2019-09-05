'''Write a letter_histogram program that asks the user for input, and prints a dictionary 
containing the tally of how many times each letter in the alphabet was used in the word. '''

words = input(" The words? ").upper()

letters_count_dict = {}
count = 0

for i in words:
    if not i in letters_count_dict:
        letters_count_dict[i] = 1
    else:
        letters_count_dict[i] += 1
print(letters_count_dict)

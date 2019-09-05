'''
Word Summary
Write a word_histogram program that asks the user for a sentence as its input, and prints a dictionary containing the tally 
of how many times each word in the alphabet was used in the text. 
'''
the_sentence = "To be or not to be"
change_to_cap = the_sentence.lower()
the_split_sentence = change_to_cap.split(" ")
words_count = {}

for i in the_split_sentence:
    if not i in words_count:
        words_count[i] = 1
    else:
        words_count[i] += 1
print(words_count)

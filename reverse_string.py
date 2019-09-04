'''reverse_me = "Hello"
str = " "
for i in reverse_me:
    str = i + str
print(str) '''

''' Long-Long Given a word string, print the results of extending any long vowels to the length of 5 

str = "hello"
str2 = " "
for i in str:
    if i == 'a' or i == 'e' or i == 'i' or i == 'u':
       str2 += i * 5       
    else:
        str2 += i
print(str2) '''

''' Given a paragraph of text as string print the paragraph in leetsspeack

users_words = input("Give me some words can I translate them into leetspeack ? ").upper()
str = ''
# This will convert each letters to leetcode
for index in users_words:
    if index == "A":
       str += "4"
    elif index == "E":
       str += "3"
    elif index == "I":
       str += "1"
    elif index == "O":
       str += "0"
    elif index == "S":
       str += "5"
    elif index == "T":
       str += "7"
    else:
        str += index
print(str)'''

''' This an application that will get a string and print it in Caear Cipher 13 '''

your_words = "lbh zhfg hayrnea jung lbh unir yrnearq"
list0 = list('abcdefghijklmnopqrstuvwxyz')
list13 = list('nopqrstuvwxyzabcdefghijklm')
str = ""
# test = alpha_beta.index(your_words)
#print(test)i

for index_one in your_words:
    if index_one == " ":
       str += " "
    else:
     test = int(list13.index(index_one))
     str += list0[test]
print(str)
   
        



    









          
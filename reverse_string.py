'''reverse_me = "Hello"
str = " "
for i in reverse_me:
    str = i + str
print(str) '''

''' Long-Long Given a word string, print the results of extending any long vowels to the length of 5 '''

str = "hello"
str2 = " "


for i in str:
    if i == 'a' or i == 'e' or i == 'i' or i == 'u':
       str2 += i * 5       
    else:
        str2 += i
print(str2)
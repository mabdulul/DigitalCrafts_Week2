

the_sentence = "to be or not to be do be do be do"
change_to_cap = the_sentence.lower()
the_split_sentence = change_to_cap.split(" ")
words_count = {}
top_three = {}


for i in the_split_sentence:
    if not i in words_count:
        words_count[i] = 1
    else:
        words_count[i] += 1
#print(words_count)


for key, value in sorted(words_count.items(), key=lambda item: item[1], reverse = True):    
     words_count[key] = value
     if len(words_count) >= 3 and len(top_three) < 3:
       for index in words_count:
          top_three[key] = value
         
          
print(top_three)             
             






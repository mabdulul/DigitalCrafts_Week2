from pprint import pprint
from characters import characters


'''count = 0
for character in characters:
    if character['name'][0] == 'A':
        #pprint(character['name'])
        count += 1
    if character['name'].startswith('A') == True:
        #pprint(character['name'])
        count += 1
pprint(count)'''
#How many characters names start with "A"?

#How many characters names start with "Z"?
''' count_Z = 0
for character in characters:
    if character['name'].startswith('Z') == True:
        #pprint(character['name'])
        count_Z += 1
pprint(count)
'''

#How many characters are dead?
dead_count = 0 
for character in characters:
    if character["died"] == "":
        dead_count += 1
print(dead_count)

#Who has the most titles?
max_titles = 0; 
name_of_char = " "
for character in characters:
    if len(character["titles"]) > max_titles:
        max_titles = len(character["titles"])
        name_of_char = character["name"]
print(max_titles)
pprint(name_of_char)
    
#How many are Valyrian
count_val = 0;
for character in characters:
    if character["culture"] == "Valyrian":
        count_val += 1
#print(count_val)

#What actor plays "Hot Pie"
name_of_character = "";
for character in characters:
    if character["name"] == "Hot Pie":
        print(character["playedBy"])


#How many characters are *not* in the tv show?








# print(len(characters))

# # print out the key names individually
# for k in jon_snow:
#    print(k)

# # print out just the values
# for key in jon_snow:
#    print(jon_snow[key])

# # print both the key and the value
# for k in characters.jon_snow:
#    print("%s: %s" % (k, jon_snow[k]))
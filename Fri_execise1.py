#Given two arrays write a function to find out if two arrays have the same frequency of digits.
'''
list_one = [1,2,3,4]
list_two = [1,4,3,2]
list_two.sort()
list_one.sort()
if len(list_two) == len(list_one):
    if list_one == list_two:
        print("True")
    else:
        print("Flase")
else:
    print("They do not have the same freq")
'''
#Given two arrays write a function to determine if each value in our first array contains a corrsponding value
#to the second power in the second array.

three = [1,2,3,4]
four = [1,4,3,2]

for index_four in three:
        for index_three in four:
            while index_four * 2 == index_four:
                    print("true")
            else:
                print("false")

















    
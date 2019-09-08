#Excersie 1 

class Person:
    
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.friends = []
        self.phone = phone
        self.greeting_count = 0
    def __str__(self): 
        return 'Person: {} {} {}'.format(self.name, self.email, self.phone)
    def add_friend(self,friend):
        self.friends.append(friend)
    def num_friends(self):
        return len(self.friends)
    def greet(self, other_person):
        self.greeting_count += 1
        return 'Hello {}, I am {}!'.format(other_person.name, self.name) 
    def print_contact_info(self):
        return "{}\'s email: {}, {}\'s phone number: {}".format(self.name,self.email, self.name, self.phone)


Sonny = Person("Sonny","sonny@hotmail.com", "678-927-4983")
Jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
Jordan.add_friend("Sonny")
Sonny.add_friend("Jordan")
Sonny.add_friend("Sean")

print(Sonny.friends)
print(Sonny.num_friends())
print(str(Jordan))


print(Sonny.greet(Jordan))
print(Sonny.greet(Jordan))
print(Sonny.greet(Jordan))
print(Sonny.greeting_count)





#print(Sonny.greet(Jordan))
#print(Jordan.greet(Sonny))
#print("Email:"+Sonny.email+" Phone:" +Sonny.phone)
#print("Email: %s Phone: %s" % (Jordan.email , Jordan.phone)) 
#print(Sonny.print_contact_info())



#-----------------------------------------------------------------------------------------------------------------------

#Make your own class

'''  class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year 
    def print_info(self):
        return 'Year: {} Make: {} Model: {}' .format(self.year, self.make, self.model) 
    def print_contact_info(self): 


#car_one = Vehicle('Nissan', 'Leaf', 2015)
#print(car_one.print_info())'''


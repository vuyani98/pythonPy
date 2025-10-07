#collections - list, tuple, set, dictionary


#Lists
evenNumbers = [2,4,6,8,10] #a list is mutable

evenNumbers.append(12) #adding an element to the list
evenNumbers.remove(4) #removing an element from the list


for number in evenNumbers:
    #print(number)
    pass


#Tuples (similar to lists but immutable)
oddNumbers = (1,3,5,7,9) #a tuple is immutable

#print(oddNumbers[0]) #accessing an element from the tuple
#oddNumbers.append(11) #this will raise an error because tuples are immutable


#Dictionaries (key-value pairs)
person = { "name": "John", "age": 30, "city": "New York"} #a dictionary is mutable

#print(f"{person["name"]} is {person["age"]} years old!")


#iteration over dictionary
for key, value in person.items():

    if (key == "age"):
        #print(f"{key}: {value}")
        pass

#method to add a year to the age
def add_year(person):
    #add 1 to the age
    person["age"] += 1
    return person["age"]


new_age = add_year(person)

print(f"New age is: {new_age}")
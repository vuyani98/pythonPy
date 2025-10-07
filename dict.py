
students = {
    "s001" : {"name": "Alice", "age": 20, "major": "Computer Science"},
    "s002" : {"name": "Bob", "age": 22, "major": "Mathematics"},
    "s003" : {"name": "Charlie", "age": 21, "major": "Physics"}
}


#iteration over nested dictionary
for key, value in students.items():

    #print(key[0])
    
    for inner_key, inner_value in value.items():

        if (inner_key == "name"):

            #print(f"Student number: {key} is {inner_value}")
            pass

#print(students["s002"]["major"]) 


#students.pop("s003") #removing an element from the dictionary
students.popitem() #removing the last inserted element from the dictionary

students["s004"] = {"name": "David", "age": 23, "major": "Chemistry"} #adding an element to the dictionary

students["s004"]["minor"] = "Biology" #adding a new key-value pair to an existing dictionary

print(students)
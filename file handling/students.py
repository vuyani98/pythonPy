import json

#handling json
file  = open("data.json", 'r') #opened file

#load
file_data = json.load(file) #convert json to python dictionary

print(file_data)

#loads
jsonString = '{"students" : [{ "name" : "John", "age" :24 }, { "name" : "Jane","age" : 28}]}'

str_data = json.loads(jsonString)

print(str_data)

file.close() #close file


#writing to a json file

file = open("data.json", 'w') #reopen file

new_student  = { "name": "Sam", "age": 22}

file_data["students"].append(new_student)

json.dump(file_data, file, indent=4)

file.close()





import csv

#read the csv file
file = open('employees.csv', 'r')

fileReader = csv.reader(file)
next(fileReader)  # Skip the header row

for employee in fileReader:
    print(employee) #each employee is a list
    pass


file.close()

#write to the csv file
new_file = open('employees2.csv', 'w')

fileWriter = csv.writer(new_file)
fileWriter.writerow(['name', 'department', 'salary'])

fileWriter.writerow(['Sbu', 'IT', 12000])

new_file.close()


file = open('employees.csv', 'r')
fileReader = csv.DictReader(file)
for employee in fileReader:
    print(f"Name: {employee['name']}, Department: {employee['department']}, Salary: {employee['salary']}")

file.close()


#append dict to a csv file
file = open('employees.csv', 'a', newline='\n')
fileWriter = csv.DictWriter(file, fieldnames=['name', 'department', 'salary'])
fileWriter.writerow({'name': 'Lerato', 'department': 'Marketing', 'salary': 9000})
file.close()


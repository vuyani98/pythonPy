
# open function takes in 2 params, the first is the file name and the second is the mode
# modes: 'r' - read, 'w' - write, 'a' - append, 'r+' - read and write
myFile = open('hello.txt', 'r')

#reading file
#print(myFile.read())


#always close the file
myFile.close()

#writing to a file
myFile2 = open('hello.txt', 'w')

myFile2.write('My name is Bond, James Bond.')

myFile2.close()

#appending to a file
myFile3 = open('hello.txt', 'a')
myFile3.write('\n And i drive an Aston Martin')
myFile3.close()


#reading and writing
myFile4 = open('hello.txt', 'a+', newline='\n')

myFile4.write('This is the End')

print(myFile4.read())
myFile4.close()






evenNumbers = {2,4,6,8,10} 
primeNumbers = {2,3,5,7,11}

#print(evenNumbers.union(primeNumbers)) #union of two sets
print('Union of two sets:')
print(evenNumbers | primeNumbers)

for number in evenNumbers:
    #print(number)
    pass

#print(evenNumbers.intersection(primeNumbers)) #intersection of two sets
print('Intersection of two sets:')
print(evenNumbers & primeNumbers)

print('Difference of two sets:')
print(primeNumbers - evenNumbers) #difference of two sets

evenNumbers.add(12) #adding an element to the set
print(f"New even numbers set: {evenNumbers}")

# Read packages into Python library:
import numpy as np

# Array
cars = ["Ford", "Volvo", "BMW"]

#Iteration through array
for x in cars:
  print(x)
print('**************************')
#Elements are mutable

cars[0] = "Ferrari"

for x in cars:
  print(x)
print('**************************')
#Elements can be duplicate

cars.append("Ferrari")

for x in cars:
  print(x)
print('**************************')
# Set Example its elements are immutable

my_set = {1, 2, 3}
print(my_set)
print('**************************')
#Iteration through Set

for val in my_set: 
    print(val)
print('**************************')
# You can add/remove elements to a set. It can be mixed data type

my_set.add('New element')

for val in my_set: 
    print(val)
print('**************************')
my_set.remove(1)

for val in my_set: 
    print(val)
print('**************************')

#You can not have duplicate elements in set
my_set.add('New element')
for val in my_set: 
    print(val)
print('**************************')


#List
thislist = ["apple", "banana", "cherry"]
print(thislist)
print('**************************')

#Iteration through list
for i in thislist: 
    print(i)
print('**************************')    
# You can add/remove elements to a list. It can be mixed data type

thislist.append('New element')

for val in thislist: 
    print(val)
print('**************************')
thislist.remove("banana")

for val in thislist: 
    print(val)
print('**************************')

#You can have duplicate elements
thislist.append('New element')
for val in thislist: 
    print(val)
print('**************************')


# numpy array 
 
# Create an array with random values 
e = np.random.random(10) 
print ("\nA random array e=:\n", e)
print('**************************')

e = np.append (e, [10, 11, 12])

print(e)
print('**************************')

#vector operations

e= e* 2
print ("\n e*2=:\n", e)
print('**************************')

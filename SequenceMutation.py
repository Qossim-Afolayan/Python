#list Mutation
fruit = ["banana", "apple", "cherry"]
print(fruit)

fruit[0] = "pear"
fruit[-1] = "orange"
print(fruit)

alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = ['x', 'y']
print(alist)

#Removing
alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = []
print(alist)

#Inserting
alist = ['a', 'd', 'f']
alist[1:1] = ['b', 'c']
print(alist)
alist[4:4] = ['e']
print(alist)

# the behavior of obj = obj + object_two is different than obj += object_two when obj is a list. 
# The first version makes a new object entirely and reassigns to obj. 
# The second version changes the original object 
# so that the contents of object_two are added to the end of the first.

x = ["dogs", "cats", "birds", "reptiles"]
y = x
x += ['fish', 'horses']
y = y + ['sheep']

#Strings are immutable
# greeting = "Hello, world!"
# greeting[0] = 'J'            # ERROR!
# print(greeting)

greeting = "Hello, world!"
newGreeting = 'J' + greeting[1:]
print(newGreeting)
print(greeting)          # same as it was

#List Element Deletion
a = ['one', 'two', 'three']
del a[1]
print(a)

alist = ['a', 'b', 'c', 'd', 'e', 'f']
del alist[1:5]
print(alist)

# Since variables refer to objects, if we assign one variable to another,
# both variables refer to the same object - Aliasing
a = [81, 82, 83]
b = a
print(a is b)

a = [81,82,83]
b = [81,82,83]
print(a is b)

b = a
print(a == b)
print(a is b)

b[0] = 5
print(a)

#Cloning a list
a = [81,82,83]

b = a[:]       # make a clone using slice
print(a == b)
print(a is b)

b[0] = 5

print(a)
print(b)

alist = [4,2,8,6,5]
blist = alist * 2
blist[3] = 999
print(alist)
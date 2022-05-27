#Adds a new item to the end of a list
mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

#Inserts a new item at the position given
mylist.insert(1, 12)
print(mylist)

#Count - Returns the number of occurrences of item
print(mylist.count(12))

#Index - Returns the position of first occurrence of item
print(mylist.index(3))
print(mylist.count(5))

#Reverse- Modifies a list to be in reverse order
mylist.reverse()
print(mylist)

#Sort -Modifies a list to be sorted
mylist.sort()
print(mylist)

#Remove - Removes the first occurrence of item
mylist.remove(5)
print(mylist)

#Pop- Removes and returns the last item
lastitem = mylist.pop()
print(lastitem)
print(mylist)


#Append Vs Concatenate
origlist = [45,32,88]
print("origlist:", origlist)
print("the identifier:", id(origlist))             #id of the list before changes
newlist = origlist + ['cat']
print("newlist:", newlist)
print("the identifier:", id(newlist))              #id of the list after concatentation
origlist.append('cat')
print("origlist:", origlist)
print("the identifier:", id(origlist))             #id of the list after append is used

st = "Warmth"
a = []
b = a + [st[0]]
c = b + [st[1]]
d = c + [st[2]]
e = d + [st[3]]
f = e + [st[4]]
g = f + [st[5]]
print(g)
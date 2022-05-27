#The is operator will return true if the two references are to the same object. 
#which is the case for strings
a = "banana"
b = "banana"

print(a is b)
print(id(a))
print(id(b))

# Here, a and b refer to two different lists, each of which happens to have the same element values. 
# They need to have different ids so that mutations of list a do not affect list b.
a = [81,82,83]
b = [81,82,83]

print(a is b)

print(a == b)

print(id(a))
print(id(b))

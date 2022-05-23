colors = ["blue", "yellow", "brown", "White", "Orange"]
name = "Steve Oney"

print("I didn't save the file before printing it to the console")
print(colors[2:3])
print(name)

print(colors[len(colors) - 1])
print(colors[len(colors) // 2])

colors = ("blue", "yellow", "brown", "White", "Orange")
#Concatenation and Repetition
colours = colors[:3] + ("Purple",) + colors[3:]
print(colours)

print(colors + (1, 2, 3))

print(colors * 4)

#Count and index method
print(colours.count("Purple"))
print(colours.index("blue")) #Runtime Error

#Split and Join Method
print("Leaders and best".split("e"))
list = ["blue", "yellow", "brown", "White", "Orange"]
print(";".join(list))
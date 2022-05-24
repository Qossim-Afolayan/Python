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

'''addition_str is a string with a list of numbers separated by the + sign. 
Write code that uses the accumulation pattern to take the sum of 
all of the numbers and assigns it to sum_val (an integer).
(You should use the .split("+") function to split by "+" and int() 
to cast to an integer).'''

addition_str = "2+5+10+20"
addition_list = addition_str.split("+")

sum_val = 0
for num in addition_list:
    sum_val += int(num)
print(sum_val)

"""
week_temps_f is a string with a list of fahrenheit temperatures separated by 
the , sign. Write code that uses the accumulation pattern to compute the average
(sum divided by number of items) and assigns it to avg_temp.
Do not hard code your answer (i.e., make your code compute both 
the sum or the number of items in week_temps_f) (You should use 
the .split(",") function to split by "," and float() to cast to a float).
"""
week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
num = 0
week_temps_list = week_temps_f.split(",")
sum_val = 0
for item in week_temps_list:
    num += 1
    sum_val += float(item)
    
avg_temp = sum_val / num
print(avg_temp)

"""
Write code to create a list of word lengths for the words in original_str 
using the accumulation pattern and assign the answer to a variable num_words_list. 
(You should use the len function).
"""
original_str = "The quick brown rhino jumped over the extremely lazy fox"

words_list = original_str.split()
num_words_list = []
for word in words_list:
    num_words_list.append(len(word))
    
print(num_words_list)
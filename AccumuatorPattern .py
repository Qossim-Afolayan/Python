#Before accumuating:
"""
1. What sequence will you iterate through as you accumulate a result? 
It could be a range of numbers, the letters in a string, 
or some existing list that you have just as a list of names.
"""
"""
2. What type of value will you accumulate? If your final result will be a number,
your accumulator will start out with a number and 
always have a number even as it is updated each time. Similarly, 
if your final result will be a list, start with a list.
If your final result will be a string, you’ll probably want to start with a string;
one other option is to accumulate a list of strings and 
then use the .join() method at the end to concatenate them all together.
"""

nums = [3, 5, 8]
accum = []
for w in nums:
    x = w**2
    accum.append(x)
print(accum)

alist = [4,2,8,6,5]
blist = [ ]
for item in alist:
   blist.append(item+5)
print(blist)

lst= [3,0,9,4,1,7]
new_list=[]
for i in range(len(lst)):
   new_list.append(lst[i]+5)
print(new_list)

numbs = [5, 10, 15, 20, 25]

for i in range(len(numbs)):
    numbs[i] = numbs[i] + 5

print(numbs)    

#the order is reversed due to the order of the concatenation.
s = "ball"
r = ""
for item in s:
   r = item.upper() + r
print(r)

str1 = "I love python"
# HINT: what's the accumulator? That should go here.

chars = []
for n in str1.strip(""):
    chars.append(n)
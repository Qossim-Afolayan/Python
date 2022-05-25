#Numbers of non-space characters
phrase = "What a wonderful day to program"
tot = 0
for char in phrase:
    if char != " ":
        tot = tot + 1
print(tot)

#Checking the number of vowels in a string
s = "what if we went to the zoo"
x = 0
for i in s:
    if i in ['a', 'e', 'i', 'o', 'u']:
        x += 1
print(x)
#Accumulating the Max Value
nums = [9, 3, 8, 11, 5, 29, 2]
best_num = nums[0]
for n in nums:
    if n > best_num:
        best_num = n
print(best_num)

#Forming the past tense of a list
words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_tense = []
for word in words:
    if word[-1] == "e":
        past_tense.append(word + "d")
    else:
        past_tense.append(word + "ed")
print(past_tense)

rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
rainfall_mi_list = rainfall_mi.split(",")

num_rainy_months = 0
for inch in rainfall_mi_list:
    if float(inch) > 3:
        num_rainy_months += 1


sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

same_letter_count = 0
for word in sentence.split():
    if word[0] == word[-1]:
        same_letter_count += 1

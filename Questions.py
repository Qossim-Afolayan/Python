"""
Write code that uses the string stored in org and creates an acronym 
which is assigned to the variable acro. Only the first letter of each word should be used, 
each letter in the acronym should be a capital letter, and there should be nothing to separate the letters
of the acronym. Words that should not be included in the acronym are stored in the list stopwords. 
For example, if org was assigned the string “hello to world” then the resulting acronym should be “HW”.
"""
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"

"""
Write code that uses the string stored in sent and creates an acronym which is assigned to 
the variable acro. The first two letters of each word should be used, 
each letter in the acronym should be a capital letter, and each element of the acronym 
should be separated by a “. ” (dot and space). 
Words that should not be included in the acronym are stored in the list stopwords. 
For example, if sent was assigned the string “height and ewok wonder” then 
the resulting acronym should be “HE. EW. WO”.
"""
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
main_acro = ""
acro =""
for word in sent.split():
    if word not in stopwords:
        main_acro += (word[:2].upper() + ". ")
acro += main_acro[:-2]

#Palindrome
p_phrase = "was it a car or a cat I saw"
r_phrase = p_phrase[::-1]

"""
Provided is a list of data about a store’s inventory where each item in the list represents
the name of an item, how much is in stock, and how much it costs. Print out each item in the list with 
the same formatting, using the .format method (not string concatenation). 
For example, the first print statment should read The store has 12 shoes, each for 29.99 USD.
"""
inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
for string in inventory:
    print("The store has {} {}, each for {} USD.".format(string.split(", ")[1], string.split(", ")[0], string.split(", ")[2]))

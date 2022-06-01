ss = "Hello, World"
print(ss.upper())   #Returns a string in all uppercase

tt = ss.lower()     #Returns a string in all lowercase
print(tt)
print(ss)

ss = "    Hello, World    "

els = ss.count("l")
print(els)

print("***"+ss.strip()+"***")   #Returns a string with the leading and trailing whitespace removed

news = ss.replace("o", "***")  #Replaces all occurrences of old substring with new 
print(news)

s = "python rocks"
print(s[1]*s.index("n"))

#Format Method
scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
for person in scores:
    name = person[0]
    score = person[1]
    print("Hello {}. Your score is {}.".format(name, score))

person = input('Your name: ')
greeting = 'Hello {}!'.format(person)
print(greeting)

origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))
newPrice = (1 - discount/100)*origPrice
calculation = '${} discounted by {}% is ${}.'.format(origPrice, discount, newPrice)
print(calculation)



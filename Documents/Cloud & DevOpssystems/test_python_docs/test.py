#committing to github for practice using vscode, github codespaces, & git

#1
fruits = ["apple", "banana", "pear"]
for fruitica in fruits:
    print (fruitica)
#the output is a string. if i do print(type(fruitica)), it will say it's a string

#2
fruits = ["apple", "banana", "pear"]
print (type(fruits[0])) 
#no need for a for loop to get data type. unecessary and less clear/readable 
    
 #3   
fruits = ["apple", "banana", "pear"]
for fruitica in fruits:
    print (fruitica.capitalize())
    
#4
fruits = ["apple", "banana", "pear"]
for fruitica in fruits:
    print (fruitica.upper())
    
#5 data type with nested for loop
fruits = ["apple", "banana", "pear"]
veggies = ["broccoli", "squash", "spinach"]
for fruitica in fruits:
    for vegeta in veggies:
        print(type(fruitica), type(vegeta))

#6 data type with nested for loop as a string(f/formatted string)
fruits = ["apple", "banana", "pear"]
veggies = ["broccoli", "squash", "spinach"]
for fruitica in fruits:
    for vegeta in veggies:
        print(f"The first data type is a {type(fruitica)} and the 2nd data type is {type(vegeta)}")
        
# making 2nd commit with comment via github.dev while using linux mint
names = ["john", "George", "Benjamin"]
for founding_fathers in names: 
    print(founding_fathers.capitalize())
#capitalizes all but i only want john's first letter capitalized. Examples on how below

names = ["john", "George", "Benjamin"]
for founding_fathers in names:
    if founding_fathers == "john":
        print("John")
    else: 
        print(founding_fathers)
        
names = ["john", "George", "Benjamin"]
for founding_fathers in names:
    if founding_fathers.lower() == "john":
        print(founding_fathers.capitalize())
    else:
        print(founding_fathers)

#3rd commit for additional practice with if and else conditionals

# up next is a set of loops and conditionals using a tuple. I want to create something that gives multiple responses for incorrect answers and one for the correct one#

founding_document = ("Articles Of Confederation", "Declaration Of Independence", "U.S. Constitution")
user_input = input("The founding documents of the United States are the Declaration of Independence, the U.S. Constitution, and?: ")
while user_input.title() != :
    print("Wrong. Try again.")
    if user_input.title() != f"{founding_document[0]}":
    print("Try again")
elif user_input.title() != f"{founding_document[0]}":
    print("You some kind of redcoat? Try again.")
elif user_input.title() != f"{founding_document[0]}":
    print("I bet King George would love you. Again!")
elif user_input.title() != f"{founding_document[0]}":
    print("Bruh")
user_input = input("Correct. You're a confirmed Tier 1 American.")

# this was my first attempt on the idea. However, it is incorrect. Below will be the correct way to do it #

founding_document = ("Articles Of Confederation", "Declaration Of Independence", "U.S. Constitution")
responses = ["Wrong. Try again.", "Try again.", "You some kind of redcoat? Try again.", "I bet King George would love you. Again!", "Bruh", "My God. I can't believe what I'm seeing"]
user_input = input("The founding documents of the United States are the Declaration of Independence, the U.S. Constitution, and?: ")
i = 0 #set variable in order to set up a cycle of responses
while user_input.title() != founding_document[0]: #title will capitalize each first letter of the response to match the correct numbered value in the tuple/set
    print(responses[i]) #to take from the index
    i = (i + 1) % len(responses) #% used to cycle through remaining of all responses. will loop once end reached
    user_input = input("Answer: ")
print("Correct. You're a confirmed Tier 1 American.")

#this is the correct version for the idea. 
#additional note is that the remainder when using % or modulus for the cycling of responses is saying how much of the index is used AND where we are in the index
#reaching the final response in this case would have a remainder of 0. no responses left after this as well as going back to the first response. 
#5th commit

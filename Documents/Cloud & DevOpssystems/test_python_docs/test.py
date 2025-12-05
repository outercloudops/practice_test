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
        
!!!!!!!!!!
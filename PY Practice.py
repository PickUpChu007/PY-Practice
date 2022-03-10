# Variable Practice 
import re
from sqlite3 import DateFromTicks
from winreg import REG_RESOURCE_REQUIREMENTS_LIST
from zoneinfo import available_timezones

var_1 = "this is a test, "
var_2 = "and you pass !"
full_var = var_1 + var_2
var_3 = (f"Hello, \n" + full_var)
print(var_3)

# Array arrangement
print("test 2 \n")
x, y, z = 1, 2, 3
print(f"answer= ", x + z)

# Array slicing
list_1 = ['one','two','three','four']
print(list_1[1:3])
print(list_1[-1])

# Array index picking & str add-on
msg = f"my favorite number is {list_1[0].title()}"
print(msg)

# Array Index picking from list_1 and how -1 = last of index
print(list_1[0])
print(list_1[2])
print(list_1[-1] + list_1[3])

# Replacing Index
msg_2 = ['Two', 'Four', 'Six', 'Eight']
print(msg_2)
msg_2[0] = 'One'
print(msg_2)

# add element into array & delete particular element
msg_3 = ['Two', 'Four', 'Six', 'Eight']
msg_3.append('One')
print(msg_3)
msg_3.insert(0, 'LOL')
print(msg_3)
del msg_3[1]
print(msg_3)

#add-on onto array
msg_4=[]
msg_4.append('one')
msg_4.append('two')
msg_4.append('three')
print(msg_4)

# POP function 
msg_3 = ['Two', 'Four', 'Six', 'Eight']
print(f"This the the orginal data \n", msg_3)
popped_msg_3 = msg_3.pop()
print(f"This is the popped number \n", popped_msg_3)
print(f"This is the popped array \n", msg_3)
print(f"Chinese rich rumber is {popped_msg_3.title()}.")

# Sort list & reverse sort list
arr = ["barvo", "ace", "delta", "charles"]
arr.sort()
print(arr)

# Reverse Sort fucntion
arr = ["barvo", "ace", "delta", "charles"]
arr.sort(reverse=True)
print(arr)

# reverse sort list
arr = ["barvo", "ace", "delta", "charles"]
arr.reverse()
print(arr)

# Finding the length of a list using len function
arr = ["barvo", "ace", "delta", "charles"]
print("Total count")
len(arr)

# For Loop function, reminder use indentation in for loop
arr_1s = ['Calvin','Emilie','Mom','Dad']
for arr_1 in arr_1s:
 print(arr_1)

# Principle in for loop, example
# for cat in cats
# for dog in dogs
# for list in list_of_items

# For loop, and add on str
arr_1s = ['Calvin','Emilie','Mom','Dad']
for arr_1 in arr_1s:
 print(f"{arr_1.title()}, is cool")
 print(f"I can not wait to hang with you, {arr_1.title()}")
print("You guys are awesome!") 

# Using For loop to create numarical list
for eg1 in range(1, 11):
    print(eg1)

# Using For loop to create numarical with 2 addtion
for eg1 in range(1, 12, 2):
    print(eg1)

# power of 2 for arry between 1 ~ 10 ########
squares = []
for value in range(1, 11):
    square = value **2
    squares.append(square)
print(squares)

# [More efficient coding] power of 2 for arry between 1 ~ 10
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

#[Even more efficient coding] power of 2 for arry between 1 ~ 10 "list comperhension"
squares = [value**2 for value in range(1,11)]
print(squares)

# simple statistics with list of numbers
digits = [1,2,3,4,5,6,7,8,9,0]
min(digits)
max(digits)
sum(digits)

# slicing a list
players = ['Calvin','Emilie','Mom','Dad','Tippy']
print(players[0:3])
print(players[1:3])
print(players[:3])
print(players[0:])
print("Here are the first 3 players on my list")
for player in players[:3]:
    print(player.title())

# Copying a list with slice
my_list = ['Red','Balck','White','Pink','Blue']
my_friends_list = my_list[:]
print("My favorite colors are:")
print(my_list)
print("My friends favirute colors are: \n")
print(my_friends_list)
my_list.append('Green')
my_friends_list.append('yellow')
print("My favorite colors are:")
print(my_list)
print("My friends favirute colors are: \n")
print(my_friends_list)

# Tuples function... => [] for unchangable function, eg. below
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
dimensions[0] = 250
print(dimensions[0])

# Tuples function modification using "for loop"
dimensions = (200, 50)
print("Orginal List: \n")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("Modified List: \n")
for dimension in dimensions:
    print(dimension)

# IF statement with FOR LOOP
cars =['toyota','honda','subaru','audi','bmw']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Conditional test, True ir False; rememebr it is case sensitive
car = 'bmw'
car == 'bmw'

car = 'bmw'
car == 'toyota'

car = 'Bmw'
car == 'bmw'

car = 'Bmw'
car.lower() == 'bmw'
print(car)

# Check for inequality != is equal not
topping = 'cheese'
if topping != 'shroom':
 print("its no Mario")

# Check numerical inequality
num_1 = 18
if num_1 != 20:
 print("Legal age")

# Numerical compersion & checking multiple conditions with "and" & "or"
age = 18
age_1 = 50
age > 42 #false
age < 42 #true
age <= 42 #true
age >= 42 #false
age <= 42 and age_1 >= 42 #true
age >=42 and age_1 <= 42 #false
age >= 42 or age_1 >= 42 #true

# Checking if the value is in the list
col = ['balck','pink','red','yellow','green']
'orange' in col #false
'red' in col #true
col_1 = 'orange'
if col_1 not in col:
    print(f"{col_1.title()}, is not in the list")

# Boolean Express, codition only true or false...?

# Simple IF statement
age = 18
if age >= 18:
    print("You are old enough to vote !")

# IF-ELSE STATEMENT
age = 17
if age >= 18:
    print("You are old enough to vote !")
    print("Go VOTE NOW!")
else:
    print("Too young kiddo.")

# Using simple IF-ELSE Statement
age = 18
if age >= 18:
    print("Good")
else:
    print("Bad")

# Using IF-ELSE STATEMENT with input [BAD CODE]
age = (input("Enter your age"))

if age >= 18:
    print("Good")
else:
    print("Bad")

# Using elif statement
age = 12

if age > 4:
    print("It is free")
elif age < 18:
    print("It is $5 dollars")
else:
    print("Full price adult $25")

# Using elif statement with inser strings
age = 6
if age < 4:
    price = 0
elif age < 18:
    price = 10
else:
    price = 25
print(f"Your entry fee is ${price}.")

#  ???
age = int(input())
if age >=18:
    print("dwag")
else:
    print("swag")

# Testing Multiple conditions
requested_toppings = ['olive','extra cheese']
if 'olive' in requested_toppings:
    print("adding olives.")
if 'bell pepper' in requested_toppings:
    print("adding pepper.")
if 'extra cheese' in requested_toppings:
    print("adding extra cheese")
print("\nFinished making your zar!")

# For loop, checking missing topping
requested_toppings = ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping =='green peppers':
        print("Sorry, we are out of green peppers")
    else:
        print(f"adding {requested_topping}")
print("\n FINISHED !")

# Checking if a list is not empty
requested_toppings =[]
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"adding {requested_topping}")
    print("DONE!")
else:
    print("There is nothing, YOU SURE ?")

# Using multiple lists
available_toppings = ['A','B','C','D','E','F']
requested_toppings = ['A','G','C']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry we dont have {requested_topping}.")
print("\nDONE!")

# Dictionaries, aka hash table
a_a = {'color':'red' , 'points':5}
print(a_a['color'])
print(a_a['points'])

# adding new values in dictionaries
a_a = {'color':'red' , 'points':5}
print(a_a)
a_a['x_value'] = 0
a_a['y_value'] = 25
print(a_a)

# Modifying values in a dictionary
a_a = {'color':'red' , 'points':5}
print(f"Alien color is {a_a['color']}")
a_a['color'] = 'yellow'
print(f"Now Alien color is {a_a['color']}")


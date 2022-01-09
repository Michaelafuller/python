num1 = 42 #variable declaration, data type - primitive - number
num2 = 2.3 #variable declaration, data type - primitive - number
boolean = True #variable declaration, data type - primitive - boolean
string = 'Hello World' #variable declaration , data type - primitive - string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, data type - composite - list - initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, data type - composite - dictionary - initialize
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, data type - composite - tuple - initialize
print(type(fruit)) #log statement, type check
print(pizza_toppings[1]) #log statement, data type - composite - list - access value
pizza_toppings.append('Mushrooms')# data type - composite - list - add value
print(person['name']) #log statement, data type - composite - dictionary - access value
person['name'] = 'George'# data type - composite - dictionary - change value
person['eye_color'] = 'blue'# data type - composite - dictionary - change value
print(fruit[2]) #log statement, data type - composite - tuple - access value

if num1 > 45: #conditional - if
    print("It's greater") #log statement
else:#conditional - else
    print("It's lower") #log statement

if len(string) < 5: #length check, conditional - if
    print("It's a short word!") #log statement
elif len(string) > 15: #length check, conditional - else if
    print("It's a long word!") #log statement
else: #conditional - else
    print("Just right!") #log statement

for x in range(5): #for loop - start
    print(x) #log statement, for loop - stop
for x in range(2,5): #for loop - start
    print(x) #log statement, for loop - stop
for x in range(2,10,3): #for loop - start
    print(x) #log statement #for loop - stop
x = 0 # variable declaration
while(x < 5): #while loop - start
    print(x) #log statement
    x += 1 #while loop - increment

pizza_toppings.pop() # data type - composite - list - delete value
pizza_toppings.pop(1) # data type - composite - list - delete value

print(person) #log statement
person.pop('eye_color') # data type - composite - dictionary - delete value
print(person) #log statement

for topping in pizza_toppings: # for loop - start
    if topping == 'Pepperoni': # conditional - if
        continue # for loop - continue
    print('After 1st if statement') #log statement
    if topping == 'Olives': # conditional - if
        break # for loop - break

def print_hello_ten_times(): # function - argument - none
    for num in range(10): # for loop, function - parameters
        print('Hello') #log statement

print_hello_ten_times() # function - call

def print_hello_x_times(x): # function - argument
    for num in range(x): # for loop, function - parameters
        print('Hello') #log statement

print_hello_x_times(4) # function - call - argument

def print_hello_x_or_ten_times(x = 10): # function - argument
    for num in range(x): # for loop, function - parameters
        print('Hello') #log statement

print_hello_x_or_ten_times() # function - call
print_hello_x_or_ten_times(4) # function - call - argument


""" comment multiline
Bonus section
"""

print(num3) #NameError: name <num3> is not defined
num3 = 72 # variable declaration
fruit[0] = 'cranberry' #'tuple' object does not support item assignment
print(person['favorite_team']) # KeyError: 'favorite_team'
print(pizza_toppings[7]) # IndexError: list index out of range
  print(boolean) # IndentationError: unexpected indent
fruit.append('raspberry') #AttributeError:'tuple' object has no attribute 'append'
fruit.pop(1) #AttributeError:'tuple' object has no attribute 'pop'
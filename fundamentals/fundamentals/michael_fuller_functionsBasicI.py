#1
# prediction: function returns 5
def number_of_food_groups():
    return 5
print(number_of_food_groups())


#2
# prediction: error code -- unsure of what kind. likely undefined function. should break both.
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())


#3
# prediction: returns 5; second return statement won't run
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())


#4
# prediction: function returns 5; print statement breaks - undefined
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())


#5
# prediction: function returns none
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# didn't expect the print statement to work, as well


#6
# prediction: function will add and print both iterations, then add unto itself. total will be 8
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# expected function to work. too much JS on the brain. needs (int) format to work.


#7
# prediction: will return 25
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))


#8
# prediction: first, prints 100; else statement returns 10; function ends after first return statement
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())


#9
# my goodness... prediction: first call, function returns 7
# second call, function returns 14
# third call, function returns 7 and 14 and an error code; function doesn't distinguish type int for addition
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# wrong again; the return statement allows the function to recognize int type

#10
# prediction: function returns 8, second return statement won't run
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))


#11
# prediction: print variable b, which is 500
# next, internal variable designated 300, prints 300
# next, python recognizes b as global, therefore prints 500
# function called - will it print? I think so - 300
# prints global 500 again
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# my understanding of the order was incorrect; first print of b
# function defined, but not called, therefore, the next print statement is the global b, 500
# function called, internal b defined as 300, printed
# global b printed, 500

#12
# variable defined as 500, printed
# function defined, with print and return statement, nothing printed
# function closes, print global b, 500
# function called, print 300, returns 300, function closes
# print global b, 500
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# just like JS, the difference between print and return

#13
# prediction: global b declared, printed
# function defined
# global b printed
# b redefined as function foobar()
# function called, 300 printed, returned
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# this time, as in JS, a returned statement is printed
# this is because the function has print as a parameter and the variable defined as a function was printed


#14
# prediction: function defined
# function also defined
# foo() called, 1 printed, bar() called - print 3, 2 printed
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()


#15
# prediction: function defined
# function defined
# y declared as foo()
# print function foo()
# 1 printed
# x declared as bar()
# bar() printed
# 3 printed
# 5 returned and printed
# 10 returned and printed
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
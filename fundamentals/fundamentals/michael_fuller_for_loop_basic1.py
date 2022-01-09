# Basic - print all integers 0 - 150

for x in range(0, 151):
    print(x)

# Multiples of 5 - print all multiples of 5, 5-1,000

for x in range(5, 1001, 5):
    print(x)

''' Counting the Dojo Way - print all integers, 1-100; 
if divisible by 5, print 'Coding' instead; 
if divisible by 10, print 'Coding Dojo';
'''
for x in range(1, 100):
    if x % 10 == 0:
        print('Coding Dojo')
    elif x % 5 == 0:
        print('Coding')
    else:
        print(x)

# Whoa, that sucker's huge - add odd integers 0 - 500,000, and print final sum

# sum = 0
# for x in range(-1, 500000, 2):
#     sum = sum + x
# print(sum)

sum = 0
for x in range(0, 500000):
    if x % 2 != 0:
        sum += x
print(sum)

# Countdown by Fours - print positive numbers, starting at 2018, counting down by fours

for x in range(2018, -1, -4):
    print(x)

''' Flexible Counter - set three variables: lowNum, highNum, mult. 
Starting at lowNum and going through highNum, print only the integers that are a multiple of mult.
For example, if lowNum=2, highNum=9, and mult=3, the loop will prin 3,6,9 (each line)
'''

lowNum = 1
highNum = 40
mult = 3

for x in range(1, 40):
    if x % 3 == 0:
        print(x)

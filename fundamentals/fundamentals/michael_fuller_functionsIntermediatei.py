# 1 update values in dictionaries and lists

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1 change value 10 in x to 15
x[1][0] = 15

# 2 change the last_name of first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'

# 3 in the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'

# 4 change the value 20 in z to 30
z[0]['y'] = 30

# 2 iterate through a list of dictionaries
# function loops through a list of dict and prints each key and value

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(students):
    for x in students:
        print(x)

iterateDictionary(students)

# 3 given a list of dict and a key name, function prints the value stored in that key for each dict

def iterateDictionary2(key_name, some_list):
    for x in range(0, len(some_list)):
        print(some_list[x][key_name])

iterateDictionary2('last_name', students)

# 4 iterate through a dict with list values
# create function - given a dict whose values are lists, print name of each key along with size of list
# then prints the values within each key's list

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    locationLength = len(some_dict['locations'])
    print(f'{locationLength} Locations')
    for x in some_dict['locations']:
        print(x)
    instructorLength = len(some_dict['instructors'])
    print(f'\n{instructorLength} Instructors')
    for x in some_dict['instructors']:
        print(x)


printInfo(dojo)

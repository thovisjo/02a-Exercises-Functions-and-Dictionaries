'''

02a Exercises

These skills can be used in assignment 2. These exercises are designed to teach you about some more complex data and control structures

To answer these exercises, open the IDLE program that came with your Python installation. IDLE is a line-by-line Python interpreter.
You can copy lines from this file into IDLE to interpret them and produce a result. Then copy the result back to the following line in this file (after the #).
You will also need to answer several questions to show you understand what is happening. 


'''
# Paste the following lines into IDLE, and then enter the result in the comment following the block
example_list = [1,17,20]
s = 0
for e in example_list:
	s += e
print(s)
#
# What do these five lines of code do?
# These five lines add each element in the list.

# --------------------------------------------------

# Paste the following lines into IDLE, and then enter the results in the comments following the block
example_set = {1,2,3,4,2,3,1,4,3,2,1}
print(example_set)
for c in range(3,10):
	if c in example_set:
		print('{count} is in the set'.format(count=c))
example_set_2 = {4,5,6,7}
example_set = example_set - example_set_2
print(example_set)
set_to_list = list(example_set)
print(set_to_list)
# {1, 2, 3, 4}
# 3 is in the set
# 4 is in the set
# {1, 2, 3}
# (1, 2, 3)
# What qualities of a python set do you see in the (above) example?
# The set includes only numbers that weren't repeated.
# In what situations might a python set be a useful data structure?
# When you want to count a number or object once, but it appears multiple times, a set would be useful.

# --------------------------------------------------

# Paste the following lines into IDLE, and then enter the results in the comments following the block
example_dictionary = { 'class':'Z-399', 'teacher':'Jason Francis', 'time':9.0, 5:12345 }
print(example_dictionary)
print(example_dictionary[5])
example_dictionary['time'] = '9:00'
print(example_dictionary)
students = ['James','Paige','George','Ruth','Gwen','Claire']
example_dictionary['students'] = students
print(example_dictionary)
print(example_dictionary['students'][2])
# {'class': 'Z-399', 'teacher': 'Jason Francis', 'time': 9.0, 5: 12345}
# 12345
# {'class': 'Z-399', 'teacher': 'Jason Francis', 'time': '9:00', 5: 12345}
# {'class': 'Z-399', 'teacher': 'Jason Francis', 'time': '9:00', 5: 12345, 'students': ['James', 'Paige', 'George', 'Ruth', 'Gwen', 'Claire']}
# George
# What qualities of a python dictionary do you see in the (above) example?
# It utilizes keys and it is in an undetermined order.
# Write a python dictionary that might describe a bicycle. I'll get you started. Think about what qualities a bicycle could have (top speed, mileage, pedals, seat height, etc)
bicycle = { 'color':'red', 'wheels':['front', 'back'], 'speed':90, 'basket':True, 'pedals':['left', 'right'], 'price': 700, 'owner':''}

# --------------------------------------------------

# Paste the following lines into IDLE, and then enter the results in the comments following the block
def product_list(example_list):
	s = 1
	for e in example_list:
		s *= e
	return s
r = product_list([1,2,3])
print(r)
print(product_list([2,5,6]))
print(product_list([-2,3,-4,5,-6]))
#6
#60
#-720
# What is happening in the (above) example?
# elements of the list are being added and multiplied.

# --------------------------------------------------

# Paste the following lines into IDLE, and then enter the results in the comments following the block
def is_leap_year(year):
	'''
	year is an integer that represents a year in the Gregorian calendar, and is_leap_year describes the policy of whether a given year will have 366 days
	A leap year is every fourth year, except when that year is divisible by 100, except when that year is divisible by 400
	'''
	leap = False
	try:
		if year % 400 == 0:
			leap = True
		elif year % 100 == 0:
			leap = False
		elif year % 4 == 0:
			leap = True
	except TypeError:
		leap = False
	return leap
years = [2017,2018,2000,2100,2400,"This isn't even a year"]
for y in years:
	if is_leap_year(y):
		print(str(y) + ': I get an extra day this year!')
	else:
		print(str(y) + ': Just 365 for me')
# 2017: Just 365 for me
# 2018: Just 365 for me
# 2000: I get an extra day this year!
# 2100: Just 365 for me
# 2400: I get an extra day this year!
# This isn't even a year: Just 365 for me
# What is happening in the (above) example?
# The method checks if the year is a leap year by modulus.
# What is the purpose for the multi-line comment at the beginning of the is_leap_year function?
# This is a doc string explaining what a leap year is
# What happens if you pass a value to the function that isn't a year? Why?
# It returns leap as false because it isn't a year.

# --------------------------------------------------

# Paste the following lines into IDLE, and then enter the results in the comments following the block
def is_fizz(test):
	if not isinstance(test,int):
		return False
	if test % 3 == 0:
		return True
	return False
def is_buzz(test):
	if not isinstance(test,int):
		return False
	if test % 2 == 0:
		return True
	return False
for i in range(0,10):
	if is_fizz(i) and is_buzz(i):
		print('%d: fizzbuzz'%i)
	elif is_fizz(i):
		print('%d: fizz'%i)
	elif is_buzz(i):
		print('%d: buzz'%i)
	else:
		print(i)
# 0: fizzbuzz
# 1
# 2: buzz
# 3: fizz
# 4: buzz
# 5
# 6: fizzbuzz
# 7
# 8: buzz
# 9: fizz
# What is happening in this example?
# This tests whether an object is divisible by 3 or 2 without any remainder. 
# How would you alter the program so that it prints fizz on multiples of 5 and buzz on multiples of 4?
# Simpky change the numbers in the if statement from 3 to 5 and 2 to 4.
# We actually don't want the program to print fizzbuzz when i <= 0. How would you fix this problem?
# and not 0 could be placed at the if statements of the modulus
# How would you alter the program so that it prints your name whenever both conditions are met?
# change the first line the the for statement from print 'fizzbuzz' to print('Tanner')

# --------------------------------------------------

# Paste the following lines into IDLE, and then enter the results in the comments following the block
def get_option(options):
	'''
	Prints out the choices for this location and invites the player to make a selection
	Parameters: options is a list of dictionaries {choice, location}; choice is a string and location is an int
	Returns: location if one is available and selected, 0 otherwise
	'''
	to_return = 0
	if len(options) == 0:
		print('The end!')
		return to_return
	while to_return == 0:
		choice = 1
		for o in options:
			print('{which_option}: {description}'.format(which_option=choice, description=o['choice']))
			choice += 1
		print('q: to quit')
		decision = input('Which option do you choose? ')
		try:
			if decision == 'q':
				return 0
			decision = int(decision)-1
			if decision >= 0 and decision < len(options):
				to_return = options[decision]['location']
		except ValueError:
			print('Please enter one of the options')
			to_return = 0
	return to_return
			
	
script = [
	{
		'location':1
		,'description':'It was a dark and stormy night. The door is locked.'
		,'options':[
			{'choice':'Open the door','location':2}
			,{'choice':'Run away','location':3}
		]
	},
	{
		'location':2
		,'description':'I said it was locked!'
		,'options':[]
	},
	{
		'location':3
		,'description':'Coward!'
		,'options':[]
	}
]
starting = 0
get_option(script[starting]['options'])
# What is happening in this block of code?
# This block of code is describing different locations in the dictionary of script.
# What does the get_option function do?
# it prints the choices that the player has and the description of the location.
# How would you display the description of the current location?
# You would put get_option() and put the location you wanted in the parenthesis.
# How would you display the description of the next location (after selecting an option)?
# You would do the same thing with each option as named.

print("hello world!")

# fast easy comment
'alternative to comment above'
'''
use this for longer block of comments
it can easily comment several lines
'''

# Variables
'''
Drawn on board 
int x = 100 (Java, must declare data type)
x = 100
can put any value in a variable
the value determines the data type
'''
x=100
y=5.5
x='hello'
x=[1,2,3]

# Math operations
# result is always a float
intx=100
inty=10
result=intx/inty
print(result)
# cast result to int
result=int(result)
print(result)

# an alternative is floor division which will discard any remainder
result = intx // inty
print(result)

# math module built in functions
min_val= min(10, 1)
print(min_val)
raised=pow(2,4)
print(raised)
# faster way
raised = 2**4
print(raised)

# the full Python documentation including all built in functions can be found here:
# https://docs.python.org/3/library/index.html

# if statements and concatenating output
# blocks of code are not put in curly brackets 
# indentation is required
x = -1
y = 1
if x < 0:
    print('x is less than 0')
    x += 1

if x < 0 and y > 0:
    print('x and y within range')

if x < 0 or y < 0:
    print('x or y less than 0')

if x < 0:
    print('the value of x is', x, 'and it is less than 0')
elif x > 0:
    print('x is greater than 0')
else:
    print('x is 0')

# loops - for loop and while loop
counter = 0
while counter < 10:
    print(counter)
    counter += 1

'''
for loops are traditionally used to iterate through a list of items
In Java and JavaScript they lool like for (int i=0;i<array.length;i++)
Python's for loop does not look like that. There are a few options for the 
for loop.
Here we loop through a range of values starting at 0.
'''
a_list=[10,20,30,40,50]
for i in range(5):
    print(i, a_list[i])

# 3 loop class examples
nums = [10,20,30,40,50]
for i in range(len(nums)):
    print(nums[1])

for vals in nums: # "nums" can be any variable you want 
    vals += 5
    print(vals)
print(nums)

for i, val in enumerate(nums):
    print("i is", i, "and val is", val) # seperate strings and variables with comma


dogs = ["boomer","rocky","daisy"]
print(dogs)

nums = [1,2,3,4,5]
sum_nums = 0
for num in nums:
    sum_nums += num
print("sum of nums is",sum_nums) # print using comma (can only use + to concatenate strings NOT ints)
print(f"the sum of nums is {sum_nums}") # print using f, to imbed an int within a string (not in pyth basics)

def hello(name = "friend"):
    print("hello!",name)
hello("Bob")
hello() # will call default if someone uses the function without a parameter
    



# you can also use the len function to loop through the length of the list
# here we print each item and change the default ending of a new line to a space
# the print function takes an optional parameter, end where we can define how we want
# to separate each item printed.
# items will be printed next to each other instead of on a new line
for i in range(len(a_list)):
    print(a_list[i], end=" ")
print()

# You can also iterate backwards
# first parameter is the start - end of list len(list) -1
# next is where to end the decrement at -1
# next is value to decrement by
for i in range(len(a_list)-1, -1, -1):
    print(a_list[i])

'''
The other option is to use the enumerate function
enumerate takes a list of items and returns the index place and value
and stores them in assigned variables. In this example, it stores the
index place in i and the value in val.
'''
for i, val in enumerate(a_list):
    print(i, val)

# the final most simple loop is like the for each loop in Java
# here each item of the list is assigned to value on each iteration
for value in a_list:
    print(value)

# define a function like this
def hello_world():
    print("Hello World")

# functions with a parameter 
def hello(name):
    print("Hello",name)

# Python functions accept default arguments
def hello1(name="Bob"):
    print("Hello",name)

hello_world()
hello1('Alice')
hello("James")

# Strings are a list of characters
f_name='kathleen'
l_name='malone'
full_name=f_name + " " + l_name

# access characters in a String with an index place
first_char=full_name[0]

# Python has a short cut to access elements starting from the end of the list using negative index places
# This works with any list not just strings
last_letter = full_name[-1]
print(last_letter)
second_last = full_name[-2]
print(second_last)

# Slice a string or a list
# string[start_index:end_index-1]
first_two_chars = full_name[0:2]
print(first_two_chars)
last_two_chars = full_name[-2:]
print(last_two_chars)

f_name=full_name[:8]
l_name=full_name[9:]
print(f_name, l_name)

# Repetition operator, *, will create a string made up of multiple copies of another
python_repeat3 = "python" * 3
print(python_repeat3)


#STRINGS (in class examples)
name = 'Guido Van Rossum'
title = "Rephactor Python"

#using quotes in the printed sentence
print('He said "hi" to his friend')
print("She's a great dancer.")

#String concatenation
fname = 'Hannah'
lname = ' Marsteller'
fullname = fname + lname
print(fullname)

#print first character fname
first_char = fname[0]
print(first_char)

#print last character lname
last_char = lname[-1]
print(last_char)

#printing name 3 times
name_3 = fname * 3
print(name_3)

# you can compare values using == do not need .equals when comparing 2 strings

#slicing 
full_name = "Kathleen Malone"
fname = full_name[0:8]

platform_computing = "platform.computing"
platform = platform_computing[0:8] #by default the starting will be 0, dont necessarily have to put it, default for end is the end of the string or list
computing = platform_computing[9:18]
print(platform)
print(computing)

#swapping values 8 and 4
#analysis of algorithms, selection sort
nums = [0,3,8,5,4]
temp = nums[2] #temporary 
nums[2] = nums[4]
nums[4] = temp
print(nums)

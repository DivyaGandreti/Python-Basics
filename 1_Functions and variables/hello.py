
print("hello world!")
#function(arguments)

name = input("what's your name?: ")
'''
variable =(assignment) function(arguments)
A variable is a container for a value in computer.
input function returns the use input in string format and we are storing it in a 'name' variable.
'''

print("Hi!", name)
print("Hi!", name, sep = '**')

'''
print syntax
parameters = postional parameters, named parameters -- what function takes
arguments = what is the value we are passing to function.
print(*objects, sep = ' ', end = '\n', file = sys.stdout, flush = False)

'''
print("Hi! ", end = '')
print(name)

print("hello \"friend\"")

print(f"hello {name}") #format the string



'''
String Methods
replace()
strip()
capitalize()
title()
split()
'''
first, last = name.split()
print(name.replace(' ',''))
print(name.strip())
print(name.strip().capitalize())
print(name.strip().title())
print(first.strip().title())

def hello(to="world"):
    print("hello,", to)

hello()
name = input("name?")
hello(name)
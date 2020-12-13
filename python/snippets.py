# SNIPPETS

# 
# -- GENERAL PYTHON THINGS --
# 

_string = "this is a test string"

# reversing a string
_reversed_string = _string[::-1]

# formatting an output string 
_a, _b = 1, 2
print(f"a is {_a} and b is {_b}")

# splitting a string into list items
_list = _string.split()
print(_list)

# 
# -- DATA STRUCTURES --
# 

# making a set from a list
_list = ['non', 'non', '3de', 'ded', 'non']
_set = set(_list)

# init a tuple
_tuple = (1, 2, 3)

# dictionary things
_dict = {"k10": 10, "k1": 1, "k2": 2, "k4": 4}
print('k3' in _dict) # False
print(_dict.get('k2')) # prints 2
_sortedkeys = sorted(_dict.keys())

# iterating through a dict
for key, value in _dict.items():
    print(f"key is {key}, value is {value}")

# list comprehensions
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split()[0] for name in names]

# lambdas

calc_mean = lambda num_list: sum(num_list)/len(num_list)

# 
# -- HOUDINI SPECIFIC --
# 

# run a python expression in hscript
# pythonexprs(_python_command)
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

# init a dict
_dict = {"key10": 10, "key1": 1, "key2": 2, "key4": 4}
print('key3' in _dict) # False
print(_dict.get('key2')) # prints 2
_sortedkeys = sorted(_dict.keys())



# 
# -- HOUDINI SPECIFIC --
# 

# run a python expression in hscript
# pythonexprs(_python_command)
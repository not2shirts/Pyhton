# Exploring tuples in Python

# Create a simple tuple
fruit = ("mango", "banana", "pineapple")
print("fruit:", fruit)

# Tuples support indexing just like lists
print("Second fruit:", fruit[1])

# Trying to change a value — this will fail since tuples are immutable
try:
    fruit[1] = "apple"
except TypeError as e:
    print("Error:", e)  # reminder: can't change tuple elements

# That's fine — let's keep going

# Another tuple
veg = ("potato", "tomato")

# Tuples can be added (concatenated) to make a new one
eat = veg + fruit
print("Combined tuple (eat):", eat)

# Trying count() without arguments — oops
try:
    eat.count()
except TypeError as e:
    print("Error:", e)  # count() needs an argument

# Let's count something that exists
print("Count of 'tomato':", eat.count("tomato"))

# Trying to append — nope, not allowed for tuples
try:
    eat.append("onion")
except AttributeError as e:
    print("Error:", e)  # again: tuples are immutable

# Original tuple is still intact
print("veg tuple:", veg)

# Tuple unpacking — pulling values out into variables
veg1, veg2 = veg
print("veg1:", veg1)
print("veg2:", veg2)

# Checking types
print("Type of veg:", type(veg))
print("Type of veg1:", type(veg1))  # just a string

# Reminder: tuples can be nested and hold anything
# But the key idea — they’re immutable!

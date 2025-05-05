

# Creating a dictionary using the dict() constructor with keyword arguments
fruit = dict(mango="yellow", apple="red", orange="orange", kiwi="green")
print("Our initial fruit dictionary:", fruit)

# Accessing a value using its key — works perfectly
print("Color of mango:", fruit['mango'])

# Trying to use an integer as a key (which we haven't defined) — this will fail
print("\nTrying to access fruit[0]...")
# This throws an error because the key 0 doesn't exist
# and also because all our keys are strings like "mango"
# Let's handle it gracefully
try:
    print(fruit[0])
except KeyError:
    print("Oops! KeyError: 0 — we tried to use an integer key, but our keys are strings.")

# Playing around with strings now
print("\nTrying to call a .key() method on a string...")
try:
    'red'.key()
except AttributeError:
    print("Nope! Strings don't have a .key() method.")

# Let's loop through the dictionary and just print the keys
print("\nLooping through the fruit dictionary (just the keys):")
for f in fruit:
    print(f)

# Let's try to print key-value pairs, but with some syntax mistakes along the way

# First attempt — incorrect syntax using colon
print("\nTrying incorrect syntax: print(f : fruit[f])")
print("→ Python doesn't like that! It needs commas or string concatenation.")

# Second attempt — trying to use string concatenation without commas
print("Trying: print(f \" : \" fruit[f])")
print("→ Still not valid Python. Maybe we need commas instead of string literals stuck together?")

# Finally, a working version using commas
print("\nCorrect way using commas:")
for f in fruit:
    print(f, ":", fruit[f])

# Now using .items() to get both keys and values at once
print("\nUsing .items() to loop through key-value pairs:")


# Correct version:
print("\nFixed version:")
for f, color in fruit.items():
    print(f, '=', color)

# Let's try a dictionary comprehension now — generating squares of numbers
print("\nCreating a dictionary of squares from 0 to 9...")
squared_num = {x: x**2 for x in range(10)}
print(squared_num)

# Clearing the dictionary — wiping all values out
print("\nClearing the squared_num dictionary...")
squared_num.clear()
print("Now it's empty:", squared_num)

# Adding a new key-value pair to our fruit dictionary
print("\nAdding grapes to the fruit dictionary...")
fruit["grapes"] = "light green"
print(fruit)

# Removing a specific item using .pop()
print("\nRemoving 'orange' using pop()...")
fruit.pop("orange")
print(fruit)


# Now using .popitem() correctly — removes the last inserted item
print("\nRemoving the last item (grapes) using popitem()...")
fruit.popitem()
print(fruit)

# Adding watermelon and then deleting it
print("\nAdding watermelon, then removing it again...")
fruit['watermelon'] = "darkgreen"
print("After adding:", fruit)
del fruit["watermelon"]
print("After deleting:", fruit)

# Time to try a nested dictionary!

# Be careful — 'class' is a reserved keyword in Python!
print("\nTrying to use 'class' as a key — not allowed if it's used as a variable name.")
print("Instead, we use it as a string key inside a dictionary.")

# Creating a nested dictionary the right way
school = {'class': {1: 50, 2: 45, 3: 54}, 'schoolid': 234}
print("Our school dictionary:", school)

# Accessing nested values
print("Getting class info:", school['class'])
print("Number of students in class 1:", school['class'][1])

# Using fromkeys to initialize a new dictionary with default values
print("\nCreating a dictionary using fromkeys()...")
keys = ["mango", "watermelon", "musk melon"]
default_val = "sweet"

flavours = dict.fromkeys(keys, default_val)
print("All fruits are sweet:", flavours)

# Trying something interesting: using the list of keys as the value
print("\nNow using the same list as the value for each key...")
flavours = dict.fromkeys(keys, keys)
print("Notice how all keys point to the same list object:")
print(flavours)

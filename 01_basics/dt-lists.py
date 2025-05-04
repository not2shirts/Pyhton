# Define a list of heroes
heros = ["superman", "spiderman", "batman", "nagraj"]
print(heros)

# Print each hero in the list
for hero in heros:
    print(hero)

# Access individual elements and slices
print(heros[3])            # Output: 'nagraj'
print(heros[2])            # Output: 'batman'
print(heros[0:2])          # Output: ['superman', 'spiderman']

# Modify an element
heros[1] = "ironman"
print(heros)               # Output: ['superman', 'ironman', 'batman', 'nagraj']

# Incorrect string assignment, splits string into characters
heros[1:2] = 'spiderman'   # Each character inserted as individual element
print(heros)

# Reset to original
heros = ["superman", "spiderman", "batman", "nagraj"]
print(heros)

# Replace slice with a single-element list
heros[1:2] = ["ironman"]
print(heros)

# Replace a larger slice with fewer elements
heros[1:3] = ['spiderman']
print(heros)

# Append and insert new heroes
heros.append('ironman')
print(heros)

heros.insert(4, 'wanda')
print(heros)

# Incorrect use of remove (by index, which causes error)
# heros.remove(4)  # This would raise ValueError

# Correct removal by value
heros.remove("wanda")
print(heros)

# Insert multiple elements at a specific slice (inserting at index 1)
heros[1:1] = ["batman", "batman", "batman"]
print(heros)

# Remove a slice from the list
heros[1:4] = []
print(heros)

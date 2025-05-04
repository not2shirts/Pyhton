# Conditionals and loops (basic for-loop usage)
brands = ["bmw", "meta", "x", "youtube"]

# Looping through each brand and printing them on the same line
for brand in brands:
    print(brand, end=" ")  # Output: bmw meta x youtube

print()  # for newline after the loop output

# List comprehension - a clean and concise way to generate lists

# Oops! Typo in 'Range' (Python is case-sensitive)
# squared_nums = [x**2 for x in Range(10)]  # Would raise NameError

# Correct usage with lowercase 'range'
squared_nums = [x**2 for x in range(10)]
print(squared_nums)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Understanding what range() gives
print(range(10))  # range(0, 10), a lazy object

# You can assign it and use it
y = range(0, 10)
print(y)  # Still shows as range(0, 10)

# Trying with a different range
print(range(50, 60))  # range(50, 60)

# Cube numbers using list comprehension
cube_num = [x**3 for x in range(50, 60)]
print(cube_num)  # [125000, 132651, 140608, ..., 205379]

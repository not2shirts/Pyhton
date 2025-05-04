# Playing with strings
str_ = "hello world"

# Accessing first character
print(str_[0])  # 'h'

# Full slice - gives a copy of the string
print(str_[:])  # 'hello world'

# Slicing to get parts of the string
print(str_[0:5])    # 'hello'
print(str_[:7])     # 'hello w'

# Slicing with steps (hops)
print(str_[0:10:2])  # 'hlowr'

# Splitting into words based on spaces
print(str_.split())  # ['hello', 'world']

# Counting how many times 'o' appears
print(str_.count('o'))  # 2

# Let's add some spaces to experiment with stripping
str_ = " hello world "

# Strip trims whitespace from both ends
print(str_.strip())  # 'hello world'
print(str_)          # original string is still unchanged

# Finding substring position
print(str_.find("world"))  # 7

# Replacing text
print(str_.replace("world", "earth"))  # ' hello earth '
print(str_)  # Original string is still the same

# Changing case
print(str_.lower())  # ' hello world '
print(str_.upper())  # ' HELLO WORLD '

# Let's store the uppercase version
str_ = str_.upper()
print(str_)  # ' HELLO WORLD '

# Let's start greeting someone
greet = str_
name = 'john'

# Whoops, typo while assigning string
# greet = 'welcomr   <- This would've caused a syntax error (missing closing quote)

greet = 'welcome'  # fixed version

# Using format placeholders
greetings = "{} to our place {}"
print(greetings.format(greet, name))  # 'welcome to our place john'

# Trying out .join() with a string
print(greet.join(name))  # Inserts 'welcome' between every letter of 'john'

# Oops! Trying non-existent method
# greet.cat(name)  -> this would raise an AttributeError

# Correct way to concatenate strings
print(greet + " " + name)  # 'welcome john'

# Trying .join() in a different way
print("-".join(greet))  # 'w-e-l-c-o-m-e'

# More mistakes: trying to use .len() (which doesn’t exist)
# greet.len() or greet.len  -> both will raise AttributeError

# Correct way to get length
print(len(greet))  # 7

# Another mistake: using .lowercase() instead of .lower()
# str_.lowercase()  -> AttributeError

# Fixing it step-by-step
str_ = str_.strip()
print(str_)  # 'HELLO WORLD'

# More string mistakes with quotes
# txt = "hello you can use "print" command"  -> SyntaxError

# Fixing quotes with escape characters
txt = "hello \"john\" welcome"
print(txt)  # 'hello "john" welcome'

# Trying raw strings
# txt = r"hi everyone i am "john"" -> This would still fail due to quote mismatch

# Proper raw string example
txt = r"hello world\nhow are you"
print(txt)  # Output: hello world\nhow are you (no newline because it's raw)

# Working with file paths (Windows style)
path = "c:\mnt\c"  # might give warning because \m is not a valid escape

# Better to use raw strings for paths
path = r"c:\mnt\c"
print(path)  # 'c:\mnt\c'

# Or escape backslashes manually
path = "c:\\mnt\\c"
print(path)  # 'c:\mnt\c'

# Ending backslash still works with escapes
path = "c:\\mnt\\c\\"
print(path)  # 'c:\mnt\c\'

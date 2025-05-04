# Basic float addition
num1 = 0.2
num2 = 0.3
print(num1 + num2)  # Output: 0.5

# Decimal module usage
import decimal
# Incorrect usage (will cause NameError)
# a = Decimal('0.5')  # Uncommenting this will raise an error

# Incorrect import (will cause SyntaxError)
# import decimal from Decimal  # Uncommenting this will raise an error

# Correct import and usage
from decimal import Decimal
a = Decimal('0.5')
b = 100
c = a + b
print(c)  # Output: 100.5

# Mixing Decimal with float raises error
d = 0.5
# c = a + d  # Uncommenting this will raise TypeError

# But float + int works
c = b + d
print(c)  # Output: 100.5

d = 0.55
c = b + d
print(c)  # Output: 100.55

# Math functions
from math import floor
print(floor(23.5444))  # Output: 23

# Using trunc without import (will raise NameError)
# trunc(2.8)  # Uncommenting this will raise an error

# Incorrect usage of math module (typo)
# math.trun(2.8)  # Uncommenting this will raise an error

# Correct usage
import math
print(math.trunc(2.8))   # Output: 2
print(math.trunc(-3.8))  # Output: -3  # closer to 0

# Bitwise operations
x = 1
print(x << 2)  # Output: 4
print(x | 2)   # Output: 3

# Random number generation
import random
print(random.random())       # Random float between 0.0 and 1.0
print(random.random())
print(random.randint(0, 10)) # Random integer between 0 and 10
print(random.randint(0, 10))
print(random.randint(0, 10))
print(random.randint(0, 10))
print(random.randint(1, 10))

# Working with card choices
# cards = [spade, king, queen, jack, heart]  # Would raise NameError
cards = ['spade', 'king', 'queen', 'jack', 'heart']
print(random.choice(cards))
print(random.choice(cards))
print(random.choice(cards))
print(random.choice(cards))
print(random.choice(cards))
print(cards)

random.shuffle(cards)
print(cards)

# Floating-point precision quirks
print(0.1 + 0.3)             # Output: 0.4
print(0.1 + 0.1 + 0.1)       # Output: 0.30000000000000004
print(0.35 + 0.93)           # Output: 1.28
print(0.35 + 0.933)          # Output: 1.283
print(0.35 + 0.1)            # Output: 0.44999999999999996

# Explanation: Binary floating-point vs decimal floating-point
# Like how 1/3 = 0.333... is infinite in decimal,
# 1/10 is infinite in binary and causes small precision errors.

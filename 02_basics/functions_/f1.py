import math

def sqr(x):
    return (x ** 2)

print(sqr(5))




def print_name():
    print("HI I am John")

def print_name(name="john"):
    print(f"Hi i am {name}")

# print_name()S
print_name("gaurav")
#Python only remembers the latest one (which expects 1 argument).

def multipy_two(a, b):
    return a*b

print(multipy_two(1, 2))
print(multipy_two("hello",  10))


# Create a function that returns both the area and circumference of a circle given its radius.

def area_and_circumference(r):
    area = 2* math.pi * (r**2)
    circumference = 2* math.pi * r

    return area, circumference


print(area_and_circumference(14))
area ,circumference = area_and_circumference(15)
print(area)

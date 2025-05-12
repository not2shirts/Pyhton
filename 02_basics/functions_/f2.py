# more on functions

cube = lambda x: x**3
print(cube(3))

# varaible number of args

def sum_all(*args):
    print(*args)
    print(args) # returns a tuple
    return sum(args)


print(sum_all(2,3,5))
print(sum_all(2,3,5, 10, 29))

# **kwargs


def print_kwargs(**kwargs):
    print(kwargs)
    for key, values in kwargs.items():
        print(f"{key} : {values}")

print_kwargs(name="gaurav", age="21")
print_kwargs(name="gaurav")
print_kwargs(superhero = "spiderman")

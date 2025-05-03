print("Hello World");

def print_num(n):
    inst =  isinstance(n, int) or isinstance(n, float)
    if inst:
        print("a number :", n)
    else:
        print("not a number : ", n)

print_num(12)

first = 1
second = 2
third = "third"

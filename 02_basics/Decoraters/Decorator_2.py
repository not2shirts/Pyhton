
# syntax : @decorator_name
# def my_function():
#     pass
# shorthand for : my_function = decorator_name(my_function)

def greet_decorator(func):
    def wrapper():
        print("👋 Hello!")
        func()
        print("😊 Have a nice day!")
    return wrapper

@greet_decorator
def say_name():
    print("I am Gaurav")

say_name()

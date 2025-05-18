
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
# @ property decorater

class MyClass:
    def __init__(self):
        self._my_attribute = None

    @property
    def my_attribute(self):
        return self._my_attribute

    @my_attribute.setter
    def my_attribute(self, value):
        if value < 0:
            raise ValueError("Value must be non-negative")
        self._my_attribute = value

    @my_attribute.deleter
    def my_attribute(self):
        del self._my_attribute

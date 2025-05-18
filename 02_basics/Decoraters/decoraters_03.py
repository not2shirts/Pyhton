import  time

def timer(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"This {func.__name__} took {end-start} time to execute")
        return result
    return wrapper

@timer
def greetings_delayed(name):
    time.sleep(3)
    print(f"Hello {name}")


greetings_delayed("Gaurav")

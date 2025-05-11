import random

weather = ["Sunny", "Rainy", "Snowy"]

current_weather = random.choice(weather)
print("Current Weather: ", current_weather)

if current_weather == weather[0]:
    print("Go for a walk")
elif current_weather == weather[1]:
    print("Read a book")
else:
    print("Build a snowman")

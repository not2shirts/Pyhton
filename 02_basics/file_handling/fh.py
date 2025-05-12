with open("sample.py", "r") as file:
    lines = file.readlines()

with open("sample.py", "w") as file:
    for line in lines:
        if "This is the added line" not in line:
            file.write(line)

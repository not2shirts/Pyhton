# check if a number is prime

num = int(input("Enter a number : "))

for i in range(2, num):
    if num%i == 0:
        print("---No the number is not prime---")
        break

if i == num-1:
    print("---THe nuMbEr Is PrIme---")


#  Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

items = ["apple", "banana", "orange", "apple", "mango"]

for item in items:
    if items.count(item) > 1:
        print(item)
        break

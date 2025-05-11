numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
count = 0
for number in numbers:
    if number >= 0:
        count = count + 1
    else:
        continue


print(count)

# Calculate the sum of even numbers up to a given number n.


num = int(input("Enter a positive integer : "))
sum = 0
for n in range (0, num+1):
    if (n%2 == 0):
        sum+= n
    else:
        continue

print("The sum of even numbers up to ", num, " is ", sum)


# Print the multiplication table for a given number up to 10, but skip the fifth iteration.

num = int(input("Enter a positive integer : "))
for n in range(1,11):
    if n == 5: continue
    print(num, " X ", n, " = ", num*n)

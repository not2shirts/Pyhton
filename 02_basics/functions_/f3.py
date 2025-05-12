# Write a generator function that yields even numbers up to a specified limit.

def generate_even_number(limit):
    for i in range(2, limit +1, 2):
        # print(i)
         return i
print(generate_even_number(10)) # 2




def generate_even_number(limit):
    for i in range(2, limit +1, 2):
        # print(i)
         yield i # saves in meomry and rembember the progress

gen_obj = generate_even_number(10)

for num in gen_obj:
     print(num)



# recursion

def factorial_calc(num):
     if (num == 1 or num == 0): return 1
     else: return num * factorial_calc(num-1)

print(factorial_calc(5))

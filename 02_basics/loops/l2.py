# Reverse a string using a loop.

text ="Hello World"
text_rev = ""


for i in range(len(text) -1, -1, -1):
    text_rev += text[i]


print(text_rev)

#  Given a string, find the first non-repeated character.


for ch in text:
 cnt = text.count(ch)
 if cnt == 1:
    print("the first non-repeated character is", ch)
    break

# Compute the factorial of a number using a while loop.

n = 6
fact = 1
while(n != 0):
   fact = fact * n
   n -= 1

print("factorial  is ", fact )

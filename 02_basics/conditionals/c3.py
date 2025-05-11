
pswd = input("Enter your password : ")
len = len(pswd)
security = ''

if( len < 6): security = 'Weak'
elif(len <= 10 ): security = 'Medium'
else: security = 'Strong'

print("Your password is : ", security)

import time

correct_password = "admin@123"

wait_time = 1
t = 0
while(t != 5 ):
    password = input("\nEnter the password : ")
    if password == correct_password:
        print("Correct Password! Welcome")
        break

    for i in range(wait_time, 0, -1):
         print("Wrong password. Please wait", i ,"seconds before retry.", end='\r')
         time.sleep(1)


    t += 1
    wait_time *= 2

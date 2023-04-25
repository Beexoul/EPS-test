import time

print("Welcome to the EPS test!")
print("we will count  as many enter as you can hit in 10 seconds.")

input("Press Enter to begin...")

start_time = time.time()

count = 0

while time.time() - start_time < 10:
    input(" Press Enter ")
    count += 1

eps = count / 10

print("****Time's up!*****")
print("****Time's up!*****")
print("You Hited", count, "Enters.")
print("Your EPS score is", eps)
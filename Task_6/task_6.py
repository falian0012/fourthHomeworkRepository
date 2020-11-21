from itertools import count, cycle
import time

print("Enter start number: ")
user_start_number = int(input())
print("Enter last number")
user_last_number = int(input())
for item in count(user_start_number):
    print(item)
    time.sleep(1)
    if item == user_last_number:
        break;


print("Enter some value`s: ")
# через пробел, например 8 7 4 9
list = input().split()
tempCount = 0
for item in cycle(list):
    tempCount += 1
    print(item)
    time.sleep(1)
    if tempCount == 5 * len(list):
        break
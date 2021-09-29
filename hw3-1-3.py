# Author: CMOB 9/29/2021

number = input("Please input an integer: ")

if int(number) % 2 == 0:
    print(number + " is divisible by 2.")
else:
    print(number + " is not divisble by 2.")
if int(number) % 3 == 0:
    print(number + " is divisible by 3.")
else:
    print(number + " is not divisble by 3.")
if int(number) % 5 == 0:
    print(number + " is divisble by 5.")
else:
    print(number + " is not divisble by 5.")

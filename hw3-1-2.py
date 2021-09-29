# Author: CMOB 9/28/2021

card1 = input("what is the value of your first card? ")
card2 = input("what is the value of your second card? ")

total = int(card1) + int(card2)

if total >= 21:
    print("You are bust.")
else:
    print("You are safe.")

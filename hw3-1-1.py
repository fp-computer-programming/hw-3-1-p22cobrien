# Author: CMOB 9/28/2021

t1_wins = input("How many wins did team 1 have? ")
t1_draws = input("How many draws did team 1 have? ")
t2_wins = input("How many wins did team 2 have? ")
t2_draws = input("How many draws did team 2 have? ")

t1_points = (int(t1_draws) + int(t2_wins))
t2_points = (int(t2_draws) + int(t2_wins))

if t1_points > t2_points:
    print("Team 1 has more points.")
else:
    print("Team 2 has more points.")

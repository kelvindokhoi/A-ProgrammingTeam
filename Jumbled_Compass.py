# Jumbled_Compass.py

# compass
# https://open.kattis.com/problems/compass

# python Jumbled_Compass.py < Jumbled_Compass_in.txt

start = int(input())
target = int(input())

clockwise = (target-start)%360

# print(clockwise,counter_clockwise)
print(clockwise if clockwise<=180 else clockwise-360)
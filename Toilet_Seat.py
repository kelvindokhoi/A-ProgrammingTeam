# Toilet_Seat.py

# toilet
# https://open.kattis.com/problems/toilet

# python Toilet_Seat.py < Toilet_Seat_in.txt

def Same(setup,rule):
    seat = setup[0]
    turn = 0
    for change in setup[1:]:
        if seat!=change:
            turn += 1
            seat = change
        if seat!=rule:
            turn += 1
            seat = rule
    return turn
def Pref(setup):
    seat = setup[0]
    turn = 0
    for change in setup[1:]:
        if change!=seat:
            seat = change
            turn += 1
    return turn
setup = input()

print(Same(setup,'U'))
print(Same(setup,'D'))
print(Pref(setup))

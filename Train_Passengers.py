# Train_Passengers.py

# trainpassengers
# https://open.kattis.com/problems/trainpassengers

# python Train_Passengers.py < Train_Passengers_in.txt

# things to check in the input:

# - The number of people in the train is <= the capacity and is >=0
# - No passenger waiting while there is room on the train.open
# - Nobody waits at the last station.
# - The train starts and end empty.

capacity, stations = map(int,input().split())
train = 0
valid = True
for nth_station in range(stations):
    people_that_left_the_train, people_that_entered_the_train, people_that_is_waiting = map(int,input().split())
    if nth_station==0:
        if people_that_left_the_train!=0:
            valid = False
    train += people_that_entered_the_train - people_that_left_the_train
    if not (people_that_entered_the_train>=0 and people_that_is_waiting>=0 and people_that_left_the_train>=0):
        valid = False
    if not (0<=train<=capacity):
        valid = False
    if people_that_is_waiting>0 and capacity-train>0:
        valid = False
    if nth_station==stations-1:
        if train!=0 or people_that_entered_the_train!=0 or people_that_is_waiting!=0:
            valid = False
print('possible'if valid else 'impossible')

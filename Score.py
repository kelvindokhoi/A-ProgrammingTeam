# Score.py

# score
# https://open.kattis.com/problems/score

# python Score.py < Score_in.txt


# each game takes 32 mins
H_point = A_point = 0
H_lead = A_lead = 0
for i in range(int(input())):
    team, score, time = input().split()
    score = int(score)
    time_min, time_sec = map(int,time.split(sep=':'))
    time_in_seconds = time_min*60+time_sec
    if i==0:
        past_time = time_in_seconds
    else:
        if H_point > A_point:
            H_lead += time_in_seconds - past_time
        elif A_point>H_point:
            A_lead += time_in_seconds - past_time
        past_time = time_in_seconds
    if team=='H':
        H_point += score
    else:
        A_point += score
if H_point>A_point:
    H_lead += 32*60 - past_time
elif A_point>H_point:
    A_lead += 32*60 - past_time
print(f"{['A','H'][H_point>A_point]} {H_lead//60}:{format(H_lead%60,'02')} {A_lead//60}:{A_lead%60:02}")
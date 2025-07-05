# Workout_for_a_Dumbbell.py

# workout
# https://open.kattis.com/problems/workout

# python Workout_for_a_Dumbbell.py < Workout_for_a_Dumbbell_in.txt

# Jim is ready to use machine 1 at time 0
# though if both Jim and another person want to start using a machine at the same time, Jim is polite enough to let the other person go first
# tim can use the machine while the other person is resting
# Jim’s usage sometimes results in the other people having to wait as well
# I should try the naive approach, and then DP it later if necessary, maybe even try branching to shorten the total time.

#a function to return the total time taken by jim and the offset


# Workout_for_a_Dumbbell.py
# https://open.kattis.com/problems/workout

temp_jim = [*map(int, input().split())]  # Jim's usage time, recovery time
jim = [[temp_jim[2*i], temp_jim[2*i+1]] for i in range(10)]
other_people_schedule = [[*map(int, input().split())] for _ in [0]*10]  # usage time, recovery time, first use
next_usage = [p[2] for p in other_people_schedule]

def do_workout(frame, idx):
    p_workout = other_people_schedule[idx][0]
    p_rest = other_people_schedule[idx][1]
    p_start = other_people_schedule[idx][2]
    one_cycle = p_workout + p_rest
    x = (frame - next_usage[idx]) % one_cycle if frame >= next_usage[idx] else frame - next_usage[idx]
    
    if x < 0:  # Jim arrives before other person's first use
        frame_after_workout = frame + jim[idx][0]
        next_usage[idx] = max(next_usage[idx], frame_after_workout)
        return frame_after_workout + jim[idx][1]
    elif x < p_workout:  # Jim arrives during usage (or at start)
        frame += p_workout - x
    # Else: Jim arrives during recovery, start immediately

    frame_after_workout = frame + jim[idx][0]
    if frame_after_workout > next_usage[idx]:
        next_usage[idx] = max(next_usage[idx] + one_cycle, frame_after_workout)
    return frame_after_workout + jim[idx][1]

t = 0
for _ in range(3):
    for idx in range(10):
        t = do_workout(t, idx)
t -= jim[9][1]
print(t)
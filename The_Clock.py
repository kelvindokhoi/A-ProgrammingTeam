# The Clock
# https://open.kattis.com/problems/klockan2

hour_angle = 0
minute_angle = 0
delta_hour_angle = 0.5
delta_min_angle = 6
clock_system = dict()
for i in range(0,720):
    angle = (-hour_angle+minute_angle)%360
    if angle not in clock_system:
        clock_system[angle] = i
    # print(angle,i)
    hour_angle += delta_hour_angle
    minute_angle += delta_min_angle

result_time = clock_system[(int(input())/10)%360]
print(f"{format(result_time//60,'02d')}:{format(result_time%60,'02d')}")


# Bungee_Jumping.py


# bungeejumping
# https://open.kattis.com/problems/bungeejumping

# python Bungee_Jumping.py < Bungee_Jumping_in.txt

from math import sqrt

def One_Instance():
    k,l, s,w = map(float,input().split())

    grav_force = 9.81*w
    if l < s:
        # rope shorter than bridge height
        return "Stuck in the air."
    elif l > s:
        # rope longer than bridge height
        t = sqrt((2*s)/9.81)
        v = 9.81*t
        if v > 10:
            return "Killed by the impact."
        return "James Bond survives."
    else:
        # rope equals the bridge height
        remain_f = 9.81*w - k*l
        if remain_f>0:
            
        # t_ff = sqrt((2*s)/9.81)
        # v_ff = 9.81*t_ff
        # delta_l = 9.81*w/k
        # t = sqrt((2*(s-l+delta_l))/9.81)
        # v = 9.81*t
        # if v > 10:
        #     return "Killed by the impact."
        # return "James Bond survives."


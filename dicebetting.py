# https://open.kattis.com/problems/dicebetting
# Dice Betting
# python dicebetting.py < dicebetting_in.txt

n_num_throws,  s_dice_side ,k_diffirent_winning_number= map(int,input().split())

from math import factorial,comb,perm
import random

def prob(n_num_throws, k_diffirent_winning_number, s_dice_side):
    total_prop = 0
    for i in range(k_diffirent_winning_number, n_num_throws+1):
        total_prop += comb(n_num_throws, i)*(1/s_dice_side)**i*(1-1/s_dice_side)**(n_num_throws-i)
    return total_prop


def Monte_Carlo_Sim(n_num_throws, k_diffirent_winning_number, s_dice_side, n_simulation):
    winning_case = 0
    for _ in range(n_simulation):
        throw_result = [random.randint(1,s_dice_side) for _ in range(n_num_throws)]
        if len(set(throw_result))>=k_diffirent_winning_number:
            winning_case += 1
    return winning_case/n_simulation

def new_prob(n_num_throws, k_diffirent_winning_number, s_dice_side):
    total_prop = 0
    for i in range(k_diffirent_winning_number,n_num_throws+1):
        total_prop += single_num(n_num_throws, i, s_dice_side)
        print(total_prop)
    return total_prop
def single_num(n_num_throws,target_diffence,s_side) -> float:
    ways_to_get_target = comb(s_side,target_diffence)*comb(n_num_throws,target_diffence) #ways to pick unique numbers X ways to pick the order
    ways_for_other_number_to_not_match = target_diffence**(n_num_throws-target_diffence)*factorial(n_num_throws-target_diffence) # ways to pick from existing numbers
    return (ways_for_other_number_to_not_match*ways_to_get_target)/(s_side**n_num_throws)

def dp_prob(n_num_throws, k_diffirent_winning_number, s_dice_side):
    if k_diffirent_winning_number>s_dice_side or n_num_throws<k_diffirent_winning_number:
        return 0
    dp = [1]+[0]*(k_diffirent_winning_number)
    for n in range(n_num_throws):
        # print(dp)
        next_throw_dp = [0]*(k_diffirent_winning_number+1)
        for nth_different_number in range(k_diffirent_winning_number):
            if dp[nth_different_number] > 0:
                next_throw_dp[nth_different_number+1] += (s_dice_side-nth_different_number)/s_dice_side*dp[nth_different_number]
                next_throw_dp[nth_different_number] += nth_different_number/s_dice_side*dp[nth_different_number]
        next_throw_dp[k_diffirent_winning_number] += dp[k_diffirent_winning_number]
        dp = next_throw_dp
        # print(dp)
    return dp[k_diffirent_winning_number]
    
# print(f"{prob(n_num_throws, k_diffirent_winning_number, s_dice_side):.07f}")
# print(f"{new_prob(n_num_throws, k_diffirent_winning_number, s_dice_side):.07f}")
print(f"{dp_prob(n_num_throws, k_diffirent_winning_number, s_dice_side):.08f}")
# print(f"{Monte_Carlo_Sim(n_num_throws, k_diffirent_winning_number, s_dice_side, 10000):.07f}")

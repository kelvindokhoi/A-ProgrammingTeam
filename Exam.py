# Exam
# https://open.kattis.com/contests/atp9uc/problems/exam

correct_friend_num = int(input())
my_ans = input()
friend_ans = input()
match = mismatch = 0

for a,b in zip(my_ans,friend_ans):
    # print(a,b)
    if a==b:
        match +=1
    else:
        mismatch +=1

total = mismatch+match

if total-correct_friend_num>=mismatch:
    print(correct_friend_num+mismatch)
else:
    print(total - correct_friend_num + match)
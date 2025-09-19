# Classrooms
# https://open.kattis.com/problems/classrooms

import bisect

count = 0
activities, num_class = map(int,input().split())
act_list = []
for _ in' '*activities:
    start,end = map(int,input().split())
    act_list.append((end,start))

act_list.sort()
classes = []

for end,start in act_list:
    selection = bisect.bisect_left(classes,-start)
    if selection==len(classes):
        if selection<num_class:
            bisect.insort(classes,-end-1)
            count+=1
        continue
    # del classes[selection]
    # bisect.insort(classes,-end-1)
    classes[selection] = -end-1
    classes.sort()

    count+=1

print(count)
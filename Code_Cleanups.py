# Code Cleanups
# codecleanups

input()
dirty_pushes = {*map(int,input().split())}
available_dirty = dict()
cleanup=0
clean_track=[]
for i in range(1,400):
    if i in dirty_pushes:
        available_dirty[i]=0
    # simulation
    if sum(available_dirty.values())+len(available_dirty)>=20:
        cleanup+=1
        available_dirty=dict()
        # clean_track.append(i)
    else:
        for key in available_dirty.keys():
            available_dirty[key]+=1

print(cleanup)
# print(clean_track)
# Cracking The Safe
from collections import deque
my_deque = deque([[[*map(int,input().split())] for _ in' '*3]])


def check(n):
    if n==[[0,0,0],[0,0,0],[0,0,0]]:
        return True
    return False

def new_mat(old,transform):
    new=old
    for i in range(3):
        for j in range(3):
            new[i][j]=(old[i][j]+transform[i][j])%4
    return new

transforms=[[[1,1,1],[1,0,0],[1,0,0]],[[1,1,1],[0,1,0],[0,1,0]],[[1,1,1],[0,0,1],[0,1,1]],
            [[1,0,0],[1,1,1],[1,0,0]],[[0,1,0],[1,1,1],[0,1,0]],[[0,0,1],[1,1,1],[0,0,1]],
            [[1,0,0],[1,0,0],[1,1,1]],[[0,1,0],[0,1,0],[1,1,1]],[[0,0,1],[0,0,1],[1,1,1]]]

def safe():
    visited=[]
    times=0
    for _ in range(262144):
        if my_deque[0] not in visited:
            if check(my_deque[0]):
                return times
            else:
                k=my_deque[0]
                my_deque.popleft()
                for transform in transforms:
                    my_deque.appendleft(new_mat(k,transform))
                visited.append(k)
    return -1

print(safe())
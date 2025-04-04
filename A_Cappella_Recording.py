# A Cappella Recording
from collections import deque

# def debug_wrapper(func):
#     def wrapper(*args, **kwargs):
#         print(f"Entering {func.__name__} with args: {args}, kwargs: {kwargs}")
#         result = func(*args, **kwargs)
#         print(f"Exiting {func.__name__} with result: {result}")
#         return result
#     return wrapper

# @debug_wrapper
def an_instance(allnotes,gap):
    alll = deque()
    alll.append([0,0])
    visited = []
    while alll:
        new = alll.popleft()
        visited.append(new)
        for i in range(new[-1]+1,len(allnotes)):
            alll.append(new+[i])
    visited = sorted(list(visited),key = lambda new:(max(allnotes[i] for i in new)-min(allnotes[i]for i in new),len(new)))
    for j in range(len(visited)):
        if max(allnotes[i] for i in visited[j])-min(allnotes[i]for i in visited[j])>gap:
            return visited[j-1]if j-1!=0 else visited[0]
    return visited[-1]


notes,gap = map(int,input().split())
allnotes = [int(input()) for _ in' '*notes]
count = 0
while True:
    removal = an_instance(allnotes,gap)
    allnotes = [allnotes[i] for i in range(len(allnotes)) if i not in removal]
    count+=1
    if not allnotes:
        break
print(count)

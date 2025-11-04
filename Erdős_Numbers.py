# Erdős Numbers
# https://open.kattis.com/problems/erdosnumbers
from heapq import heappop,heappush
from collections import OrderedDict,defaultdict

adjacency_list = defaultdict(set)
authors = OrderedDict()

while True:
    try:
        people = input().split()
        author = people[0]
        if author not in authors:
            authors[author]=None

        for i in range(1,len(people)):
            co_author = people[i]
            adjacency_list[author].add(co_author)
            adjacency_list[co_author].add(author)
    except EOFError:
        break

myH = [(0,'PAUL_ERDOS')]
people = {name: float("inf") for name in adjacency_list.keys()}

while myH:
    distance, name = heappop(myH)
    if distance<people[name]:
        people[name] = distance
        for another_person in adjacency_list[name]:
            if distance+1<people[another_person]:
                heappush(myH,(distance+1,another_person))
                
for name in authors.keys():
    d = people[name]
    print(name,d if d!=float('inf') else 'no-connection')
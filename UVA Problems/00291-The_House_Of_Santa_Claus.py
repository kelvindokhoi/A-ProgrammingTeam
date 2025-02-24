# 291-The_House_Of_Santa_Claus.py

def findPaths(pathlist,graph,curpath,edgevisited):
    if curpath//100000000==1:
        pathlist.append(curpath)
    else:
        p = curpath%10
        for neigbor in graph[p]:
            if (p,neigbor) not in edgevisited and (neigbor,p) not in edgevisited:
                edgevisited.add((p,neigbor))
                edgevisited.add((neigbor,p))
                findPaths(pathlist,graph,curpath*10+neigbor,edgevisited)
                edgevisited.remove((p,neigbor))
                edgevisited.remove((neigbor,p))
    return

graph = {i:set() for i in range(1,6)}
graph[1]={2,3,5}
graph[2]={1,3,5}
graph[3]={1,2,4,5}
graph[4]={3,5}
graph[5]={1,2,3,4}
pathlist=[]
edgevisited = set()
findPaths(pathlist,graph,1,edgevisited)
for p in pathlist:
    print(p)
# crackerbarrel.py
# python crackerbarrel.py < crackerbarrel_in.txt > crackerbarrel_out.txt && fc crackerbarrel_out.txt crackerbarrel_sample_out.txt
# Cracker Barrel Game

from collections import defaultdict

def valid_pos(i,j):
    if not(-1<i<5 and -1<j<5):
        return False
    return j<=i

def gen_gm():
    dirs = [(-1,0),(1,0),(-1,1),(-1,-1),(0,1),(0,-1)]
    def generate_moves(i,j,graph):
        moves = []
        for pi,pj in dirs:
            if valid_pos(i+2*pi,j+2*pj):
                if graph[i+pi][j+pj]!="__" and graph[i+2*pi][j+2*pj]=="__":
                    moves.append((pi,pj))
        return moves
    return generate_moves


def solve(graph,color):
    pegs = []
    movable_pegs = []
    pegs_by_color = defaultdict(list)
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j]!='__':
                pegs.append((graph[i][j],i,j))
                pegs_by_color[graph[i][j]].append((i,j))
    return False

color = input()
while color!='**':
    graph = []
    for i in range(5):
        line = input().strip()
        li_line = []
        for j in range(len(line)//2):
            li_line.append(line[2*j]+line[2*j+1])
        graph.append(li_line)
    print(graph)

    print("Possible" if solve(graph,color) else "Impossible")
    color = input()
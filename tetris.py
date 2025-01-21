# tetris

def check(state,column,piece):
    possible=0
    if piece==1:
        possible+=column
        for i in range(len(state)-3):
            if [state[i]]*4==state[i:i+4]:possible+=1
        return possible
    if piece==2:
        for i in range(len(state)-1):
            if [state[i]]*2==state[i:i+2]:possible+=1
        return possible
    if piece==3:
        for i in range(len(state)-2):
            if [state[i],state[i],state[i]+1]==state[i:i+3]:possible+=1
        for i in range(len(state)-1):
            if [state[i],state[i]-1]==state[i:i+2]:possible+=1
        return possible
    if piece==4:
        for i in range(len(state)-2):
            if [state[i],state[i]-1,state[i]-1]==state[i:i+3]:possible+=1
        for i in range(len(state)-1):
            if [state[i],state[i]+1]==state[i:i+2]:possible+=1
        return possible
    if piece==5:
        for i in range(len(state)-2):
            if[state[i],state[i],state[i]]==state[i:i+3]or[state[i],state[i]-1,state[i]]==state[i:i+3]:possible+=1
        for i in range(len(state)-1):
            if [state[i],state[i]+1]==state[i:i+2] or ([state[i],state[i]-1]==state[i:i+2]):possible+=1
        return possible
    if piece==6:
        for i in range(len(state)-2):
            if [state[i],state[i],state[i]]==state[i:i+3] or [state[i],state[i]+1,state[i]+1]==state[i:i+3]:
                possible+=1
        for i in range(len(state)-1):
            if ([state[i],state[i]-2]==state[i:i+2]) or [state[i],state[i]]==state[i:i+2]:
                possible+=1
        return possible
    if piece==7:
        for i in range(len(state)-2):
            if [state[i],state[i],state[i]]==state[i:i+3] or ([state[i],state[i],state[i]-1]==state[i:i+3]):
                possible+=1
        for i in range(len(state)-1):
            if [state[i],state[i]+2]==state[i:i+2] or [state[i],state[i]]==state[i:i+2]:
                possible+=1
        return possible
    
column,piece=map(int,input().split())
state=[*map(int,input().split())]
print(check(state,column,piece))
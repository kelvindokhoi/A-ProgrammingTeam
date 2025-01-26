# marbletree

# The vertices are numbered from 1 to n and are given in increasing order in the input. this is False. they are in random

# Original:
def find_root():
    for node in range(len(parent_of_the_node)):
        if parent_of_the_node[node] == -1:
            return node
    return -1
    
def DFS_marble(curr_node):
    total = 0
    for node in tree[curr_node]:
        total+= DFS_marble(node)
    marble_gap= marbles[curr_node] - 1
    total+=abs(marble_gap)
    marbles[curr_node]=1
    if parent_of_the_node[curr_node]!=-1:
        marbles[parent_of_the_node[curr_node]]+=marble_gap
    return total


while (n:=int(input()))!=0:
    tree=[[] for _ in range(n)]
    marbles=[0]*n
    parent_of_the_node=[-1]*n
    for i in range(n):
        vertex,num_marble,num_children,*childrenNames,=map(int,input().split())
        vertex-=1
        for j in range(len(childrenNames)):
            childrenNames[j]-=1
        #convert the num to the correct indice
        for name in childrenNames:
            parent_of_the_node[name]=vertex
        tree[vertex]=childrenNames
        marbles[vertex]=num_marble
    root = [x for x in range(n) if parent_of_the_node[x]==-1][0]
    # print(f"total moves: {DFS_marble(root)}")
    print(DFS_marble(root))

#Golfed version:

# def D(y):w=sum(D(a)for a in t[y]);r=m[y]-1;w+=abs(r);m[y]=1;m[p[y]]+=r if p[y]!=-1 else 0;return w
# while(n:=int(input())):
#  t,m,p,l=[[]for _ in' '*n],[0]*n,[-1]*n,range
#  for _ in l(n):
#   v,q,_,*c=map(int,input().split());v-=1;c=[x-1 for x in c];t[v]=c;m[v]=q
#   for x in c:p[x]=v
#  print(D([x for x in l(n)if p[x]<0][0]))

#Golfed (more compact but TLE bacause of the exec()):

# def D(y):w=sum(D(a)for a in t[y]);r=m[y]-1;w+=abs(r);m[y]=1;m[p[y]]+=r if p[y]!=-1 else 0;return w
# while(n:=int(input())):
#  t,m,p,l=[[]for _ in' '*n],[0]*n,[-1]*n,range
#  exec('v,q,_,*c=map(int,input().split());v-=1;c=[x-1 for x in c];t[v]=c;m[v]=q\nfor x in c:p[x]=v\n'*n)
#  print(D([x for x in l(n)if p[x]<0][0]))

#Chinese Version:

# exec(bytes('敤⁦⡄⥹眺猽浵䐨愨昩牯愠椠⁮孴嵹㬩㵲孭嵹ㄭ眻㴫扡⡳⥲活祛㵝㬱孭孰嵹⭝爽椠⁦孰嵹㴡ㄭ攠獬⁥㬰敲畴湲眠眊楨敬渨㴺湩⡴湩異⡴⤩㨩 ⱴⱭⱰ㵬孛晝牯张椠❮✠渪ⱝせ⩝Ɱⵛ崱渪爬湡敧 潦⁲ 湩氠渨㨩 瘠焬弬⨬㵣慭⡰湩ⱴ湩異⡴⸩灳楬⡴⤩瘻㴭㬱㵣硛ㄭ映牯砠椠⁮嵣琻癛㵝㭣孭嵶焽 映牯砠椠⁮㩣孰嵸瘽 牰湩⡴⡄硛映牯砠椠⁮⡬⥮晩瀠硛㱝崰せ⥝ ','u16')[2:])
# or 
# exec(bytes('敤⁦⡄⥹眺猽浵䐨愨昩牯愠椠⁮孴嵹㬩㵲孭嵹ㄭ眻㴫扡⡳⥲活祛㵝㬱孭孰嵹⭝爽椠⁦孰嵹㴡ㄭ攠獬⁥㬰敲畴湲眠眊楨敬渨㴺湩⡴湩異⡴⤩㨩 ⱴⱭⱰ㵬孛晝牯张椠❮✠渪ⱝせ⩝Ɱⵛ崱渪爬湡敧 硥捥✨ⱶⱱⱟ挪洽灡椨瑮椬灮瑵⤨献汰瑩⤨㬩⵶ㄽ挻嬽⵸‱潦⁲⁸湩挠㭝孴嵶挽活癛㵝山普牯砠椠⁮㩣孰嵸瘽湜⨧⥮ 牰湩⡴⡄硛映牯砠椠⁮⡬⥮晩瀠硛㱝崰せ⥝ ','u16')[2:])
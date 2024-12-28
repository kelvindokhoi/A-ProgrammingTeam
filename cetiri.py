# cetiri

a,b,c=sorted(map(int,input().split()));print(({a+g*i for i in range(4)}-{a,b,c}).pop()if(g:=min(c-b,b-a))else a)
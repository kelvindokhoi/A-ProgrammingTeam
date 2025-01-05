# deathtaxes

share=cost=0
while 1:
    n=input()
    try:
        command,x,y=n.split()
    except:
        command,x=n.split()
    if command=='buy':
        x,y=int(x),int(y)
        cost=(share*cost+x*y)/(share+x)
        share+=int(x)
    if command=='sell':
        x,y=int(x),int(y)
        # cost=(share*cost-x*y)/(share-x)
        share-=int(x)
    if command=='split':
        x=int(x)
        share*=x
        cost=cost/x
    if command=='merge':
        x=int(x)
        share=share//x
        cost*=x
    if command=='die':
        x=int(x)
        print(x*share-(x-cost)*share*0.3 if cost<x else x*share)
        break
# treasurehunt


"""
N indicates a l to the previous row
S indicates a l to the next row
W indicates a l to the previous column
E indicates a l to the next column
T indicates the location of the treasure.
K is already went.
"""
x,y=map(int,input().split());P=[[*input()] for j in[0]*x];l=i=j=0;M={'N':(-1,0),'S':(1,0),'W':(0,-1),'E':(0,1)}
while 1:
 if P[i][j]=="T":print(l);break
 if P[i][j]=="K":exit("Lost") #use exit("Message") makes it run longer
 m,n=M[P[i][j]];P[i][j]="K";i+=m;j+=n;l+=1
 if i==x or j==y or i<0 or j<0:exit("Out")


 x,y=map(int,input().split());P=[[*input()] for j in " "*x];l=i=j=0;M={'N':(-1,0),'S':(1,0),'W':(0,-1),'E':(0,1)}
while 1:
 if P[i][j]=="T":print(l);break
 if P[i][j]=="K":print("Lost");break
 m,n=M[P[i][j]];P[i][j]="K";i+=m;j+=n;l+=1
 if i==x or j==y or i<0 or j<0:print("Out");break
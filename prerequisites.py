# prerequisites

while (a:=input())!="0":
    chosenNum,ctgr=map(int,a.split())
    coursename={*map(int,input().split())}
    passC=True
    for _ in range(ctgr):
        numCourseIncat,mintake,*coursecodes=map(int,input().split())
        if mintake>len(coursename&{*coursecodes}):
            passC=False
    print(["no","yes"][passC])

# while(a:=input())!="0":s={*map(int,input().split())};p=1;exec("m,t,*c=map(int,input().split());p&=t<=len(s&{*c});"*int(a.split()[1]));print(["no","yes"][p])
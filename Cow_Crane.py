# Cow Crane
# cowcrane

def scenario1(old1,old2,new1,new2,servemeal1,servemeal2):
    timecow1 = abs(old1)+abs(old1-new1)
    timecow2 = abs(new1-old2)+abs(old2-new2)+timecow1
    if timecow1<=servemeal1 and timecow2<=servemeal2:
        return True
    else:
        return False
def scenario2(old1,old2,new1,new2,servemeal1,servemeal2):
    timecow2 = abs(old2)+abs(old2-new2)
    timecow1 = abs(new2-old1)+abs(old1-new1)+timecow2
    if timecow1<=servemeal1 and timecow2<=servemeal2:
        return True
    else:
        return False
# 3: go to cow1, put them at the same level as cow2. prioritize time limit to move cow 1 or 2
def scenario3(old1,old2,new1,new2,servemeal1,servemeal2):
    t1=t2=abs(old1)+abs(old1-old2)
    if servemeal1>servemeal2:
        t2+=abs(old2-new2)
        t1+=abs(old2-new2)*2+abs(old2-new1)
    else:
        t1+=abs(old2-new1)
        t2+=abs(old2-new1)*2+abs(old2-new2)
    if t1<=servemeal1 and t2<=servemeal2:
        return True
    return False
# 4: go to cow2, put them at the same level as cow1.
def scenario4(old1,old2,new1,new2,servemeal1,servemeal2):
    t1=t2=abs(old2)+abs(old2-old1)
    if servemeal1>servemeal2:
        t2+=abs(old1-new2)
        t1+=abs(old1-new2)*2+abs(old1-new1)
    else:
        t1+=abs(old1-new1)
        t2+=abs(old1-new1)*2+abs(old1-new2)
    if t1<=servemeal1 and t2<=servemeal2:
        return True
    return False


old1,old2 = map(int,input().split())
new1,new2 = map(int,input().split())
servemeal1,servemeal2 = map(int,input().split())
if scenario1(old1,old2,new1,new2,servemeal1,servemeal2) or scenario2(old1,old2,new1,new2,servemeal1,servemeal2) or scenario3(old1,old2,new1,new2,servemeal1,servemeal2) or scenario4(old1,old2,new1,new2,servemeal1,servemeal2):
    print('possible')
else:
    print('impossible')
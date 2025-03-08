# The Grand Adventure

# $ represents Money not b
# | represents Incense not t
# * represents Gem not j
# . represents the Ground (nothing)
from collections import deque
cases = int(input())
for i in range(cases):
    myq = deque()
    doibreak = False
    readtrip = input()
    for char in readtrip:
        if doibreak==True:
            break
        # print(myq)
        if char in '$|*':
            myq.append(char)
        elif char in "btj":
            if myq:
                getit = myq.pop()
                if getit=="$":
                    if char!='b':
                        print('NO')
                        doibreak=True
                        continue
                if getit=="|":
                    if char!='t':
                        print('NO')
                        doibreak=True
                        continue
                if getit=="*":
                    if char!='j':
                        print('NO')
                        doibreak=True
                        continue
            else:
                print('NO')
                doibreak=True
                continue
        else:pass
    if not doibreak:
        if not myq:
            print('YES')
        else:
            print('NO')
    

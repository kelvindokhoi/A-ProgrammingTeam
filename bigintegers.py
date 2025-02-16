# bigintegers.py

def convert(s1,s2,mode):
    if mode: #str1>str2
        for i in range(len(s1)):
            if s1[i]<s2[i]:return 'NO'
        return 'YES'
    else: #str2>str1
        for i in range(len(s1)):
            if s1[i]>s2[i]:return 'NO'
        return 'YES'

for i in range(int(input())):
    str1=input()
    str2=input()
    if str1<str2:
        if len(str1)<len(str2):
            print('YES')
        elif len(str1)>len(str2):
            print('NO')
        else:
            print(convert(str1,str2,0))
    elif str1>str2:
        if len(str1)>len(str2):
            print('YES')
        elif len(str1)<len(str2):
            print('NO')
        else:
            print(convert(str1,str2,1))
    else:
        print('NO')

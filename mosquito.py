# mosquito
while 1:
    try:
        M,P,L,E,R,S,N=map(int,input().split())
        for n in' '*N:
            tM=M
            M=P//S
            P=L//R
            L=tM*E
        print(M)
    except:break
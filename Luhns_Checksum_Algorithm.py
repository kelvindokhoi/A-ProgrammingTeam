# Luhns_Checksum_Algorithm.py


# luhnchecksum
# https://open.kattis.com/problems/luhnchecksum


# python Luhns_Checksum_Algorithm.py < Luhns_Checksum_Algorithm_in.txt

for L in[*open(0)][1:]:
    *digits, = map(int,L.strip());digits=digits[::-1]
    for i in range(len(digits)):
        if i&1:digits[i]=sum(map(int,str(digits[i]*2)))
    print('FAIL'if sum(digits)%10 else'PASS')

# golfed:

# for L in[*open(0)][1:]:i=1;print(['PASS','FAIL'][sum([a:=int(d),a*2-9*(a>4)][i:=~i]for d in L[-2::-1])%10>0])

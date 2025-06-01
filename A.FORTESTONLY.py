for L in[*open(0)][1:]:
 d=[sum(map(int,str(d*[1,2][i&1])))for i,d in enumerate(map(int,L.strip()))][::-1]
 print('FAIL'if sum(d)%10 else'PASS')
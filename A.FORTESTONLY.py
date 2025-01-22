c,p=map(int,input().split())
s=[*map(int,input().split())]
q,w,e,r=range,sum,len,0
if p<2:r=c+w([s[i]]*4==s[i:i+4]for i in q(e(s)-3))
elif p<3:r=w([s[i]]*2==s[i:i+2]for i in q(e(s)-1))
elif p<4:r=w([s[i],s[i],s[i]+1]==s[i:i+3]for i in q(e(s)-2))+w([s[i],s[i]-1]==s[i:i+2]for i in q(e(s)-1))
elif p<5:r=w([s[i],s[i]-1,s[i]-1]==s[i:i+3]for i in q(e(s)-2))+w([s[i],s[i]+1]==s[i:i+2]for i in q(e(s)-1))
elif p<6:r=w([[s[i]]*3==s[i:i+3]or[s[i],s[i]-1,s[i]]==s[i:i+3]for i in q(e(s)-2)])+w([s[i],s[i]+k]==s[i:i+2]for k in[1,-1]for i in q(e(s)-1))
elif p<7:r=w([[s[i]]*3==s[i:i+3]or[s[i],s[i]+1,s[i]+1]==s[i:i+3]for i in q(e(s)-2)])+w([s[i],s[i]-2]==s[i:i+2]or[s[i]]*2==s[i:i+2]for i in q(e(s)-1))
else:r=w([[s[i]]*3==s[i:i+3]or[s[i],s[i],s[i]-1]==s[i:i+3]for i in q(e(s)-2)])+w([s[i],s[i]+2]==s[i:i+2]or[s[i]]*2==s[i:i+2]for i in q(e(s)-1))
print(r)
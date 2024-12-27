# combinationlock
while (n:=input())!="0 0 0 0":
    a,b,c,d=map(int,n.split())
    print([(a-b)*9,(40-b+a)*9][b>a]+[(c-b)*9,(40+c-b)*9][c<b]+[(c-d)*9,(40-d+c)*9][d>c]+1080)
# b1=360*2
# b2=[(b-a)*9,360+b][b<a]
# b3=360
# b4=[(c-b)*9,360+c][b<c]
# b5=[(d-c)*9,360+d][d<c]
# print(b1+b2+b3+b4+b5)
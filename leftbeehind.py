# leftbeehind
# Left Beehind

while 1:
  a,b=map(int,input().split())
  if a==b==0:break
  print(["To the convention.","Left beehind.","Never speak again.","Undecided."][2 if a+b==13 else 0 if a>b else 1 if a<b else 3])
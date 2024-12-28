# basketballoneonone
# Basketball One-on-One

m=10;a=input();x=y=0
for i in range(0,len(a),2):
 if a[i]<"B":x+=int(a[i+1])
 else:y+=int(a[i+1])
 if 1<abs(x-y)and(x>m or y>m):print(["A","B"][y>x])
 if x==y==m:m+=1
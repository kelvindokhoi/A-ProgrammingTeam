# Bijele
# bijele

# print(*[x-y for x,y in zip((1,1,2,2,2,8),map(int,input().split()))])  

# print(*[x-int(y)for x,y in zip((1,1,2,2,2,8),input().split())])
# print(*[eval(x+'-'+y)for x,y in zip('112228',input().split())])

# print(*map(lambda x,y:eval(x+'-'+y),'112228',input().split()))

# print(*map(lambda x,y:int(x)-int(y),'112228',input().split()))

# print(*map(lambda x,y:x-48-int(y),b'112228',input().split()))

print(*map(lambda a,b:a%16-int(b),b'112228',input().split()))

# 49,49,50,50,50,56
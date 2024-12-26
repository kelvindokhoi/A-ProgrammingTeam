# jobexpenses

# input();print(sum([-x for x in map(int,input().split())if x<0]))


# input();print(-sum(x*(x<0)for x in map(int,input().split())))

# input();print(-sum(min(int(x),0)for x in input().split()))

input();print(-sum(filter(i<0,map(int,input().split()))))

# print(-sum(filter(int.__neg__,map(int,input().split()))))
# import re;input();print(-eval("+".join(re.findall('-\w*',input()))))
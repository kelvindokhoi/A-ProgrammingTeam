# numberfun
# Number Fun

# def isPossible(a,b,c):
#         return ["Possible","Impossible"][(abs(a-b)!=c)*(a+b!=c)*(a/b!=c)*(b/a!=c)*(a*b!=c)]

# for i in [0]*int(input()):
#         print(isPossible(*map(int,input().split())))

# for _in [0]*int(input()):a,b,c=map(int,input().split()); print(["Possible","Impossible"][(abs(a-b)!=a+b!=a/b!=b/a!=a*b!=c)])

for _ in[0]*int(input()):a,b,c=map(int,input().split());print(["Possible","Impossible"][{c}&{abs(a-b),a+b,a/b,b/a,a*b}!={c}])
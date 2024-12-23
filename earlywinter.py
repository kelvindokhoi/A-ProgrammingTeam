# earlywinter
# c, C = map(int,input().split())
# d = [*map(int,input().split())]
# print("It had never snowed this early!"if all([0 for i in range(c)if d[i]<=C])else f"It hadn't snowed this early in {next(i for i in range(c)if d[i]<=C)} years!")

# c,y=map(int,input().split())
# d=map(int,input().split())
# for i in range(c):
#  if next(d)<=y:print(f"It hadn't snowed this early in {i} years!");exit()
# print("It had never snowed this early!")

# y=int(input().split()[1])
# a="snowed this early"
# *[int(x)<=y and exit(print("It hadn't",a,"in",i,"years!"))for i,x in enumerate(input().split())],
# print("It had never",a+"!")

y=int(input().split()[1]);a=' snowed this early';*[int(x)<=y>exit(print(f"It hadn't{a} in {i} years!"))for i,x in enumerate(input().split())],print(f"It had never{a}!")
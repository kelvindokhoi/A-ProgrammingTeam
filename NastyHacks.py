for _ in [0]*int(input()):
 a,b,c=map(int,input().split());b-=c;print([n:="advertise","does not matter","do not "+n][1 if b==a else 0 if b>a else 2])









# def if_no_ad(map):
#     return map[0]
# def if_ad(map):
#     return map[1]-map[2]

# def main():
#     output = []
#     n = int(input())
#     maps = [[int(x) for x in input().split()] for _ in range(n)]
#     for i in range(n):
#         if if_no_ad(maps[i]) > if_ad(maps[i]):
#             output.append("do not advertise")
#         elif if_no_ad(maps[i]) < if_ad(maps[i]):
#             output.append("advertise")
#         else:
#             output.append("does not matter")
#     for i in range(n):
#         print(output[i])

# if __name__ == "__main__":
#     main()
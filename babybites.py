# babybites
# makesense=True
# total=int(input())
# allmumble=input().split()
# print("makes sense" if (allmumble[i]=="mumble" or allmumble[i]==str(i+1) for i in range(total)) else "something is fishy")


# print("makes sense"if all(x=="mumble"or x==str(i+1)for i,x in enumerate(input().split()[:int(input())]))else"something is fishy")
# input();print("makes sense"if all(x=="mumble"or x==str(i+1)for i,x in enumerate(input().split()))else"something is fishy")

# input();print(["something is fishy","makes sense"][all(x=="mumble"or x==str(i+1)for i,x in enumerate(input().split()))])
input();print(("something is fishy","makes sense")[all(x=="mumble"or x==str(i+1)for i,x in enumerate(input().split()))])


# input();n=input().split();print("makes sense"if all(n[i]=="mumble"or n[i]==str(i+1)for i in range(len(n)))else"something is fishy")

# for i in range(total):
#     if allmumble[i]=="mumble" or allmumble[i]==str(i+1):
#         pass
#     else:
#         makesense=False
#         break
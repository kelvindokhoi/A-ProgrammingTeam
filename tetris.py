# # tetris


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

# def check(state,column,piece):
#     possible=0
#     if piece==1:
#         possible+=column
#         for i in range(len(state)-3):
#             if [state[i]]*4==state[i:i+4]:possible+=1
#         return possible
#     if piece==2:
#         for i in range(len(state)-1):
#             if [state[i]]*2==state[i:i+2]:possible+=1
#         return possible
#     if piece==3:
#         for i in range(len(state)-2):
#             if [state[i],state[i],state[i]+1]==state[i:i+3]:possible+=1
#         for i in range(len(state)-1):
#             if [state[i],state[i]-1]==state[i:i+2]:possible+=1
#         return possible
#     if piece==4:
#         for i in range(len(state)-2):
#             if [state[i],state[i]-1,state[i]-1]==state[i:i+3]:possible+=1
#         for i in range(len(state)-1):
#             if [state[i],state[i]+1]==state[i:i+2]:possible+=1
#         return possible
#     if piece==5:
#         for i in range(len(state)-2):
#             if[state[i],state[i],state[i]]==state[i:i+3]or[state[i],state[i]-1,state[i]]==state[i:i+3]:possible+=1
#         for i in range(len(state)-1):
#             if [state[i],state[i]+1]==state[i:i+2] or ([state[i],state[i]-1]==state[i:i+2]):possible+=1
#         return possible
#     if piece==6:
#         for i in range(len(state)-2):
#             if [state[i],state[i],state[i]]==state[i:i+3] or [state[i],state[i]+1,state[i]+1]==state[i:i+3]:
#                 possible+=1
#         for i in range(len(state)-1):
#             if ([state[i],state[i]-2]==state[i:i+2]) or [state[i],state[i]]==state[i:i+2]:
#                 possible+=1
#         return possible
#     if piece==7:
#         for i in range(len(state)-2):
#             if [state[i],state[i],state[i]]==state[i:i+3] or ([state[i],state[i],state[i]-1]==state[i:i+3]):
#                 possible+=1
#         for i in range(len(state)-1):
#             if [state[i],state[i]+2]==state[i:i+2]or[state[i],state[i]]==state[i:i+2]:possible+=1
#         return possible
# column,piece=map(int,input().split())
# state=[*map(int,input().split())]
# print(check(state,column,piece))
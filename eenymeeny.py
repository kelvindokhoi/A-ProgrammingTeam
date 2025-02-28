# eenymeeny.py

# Shortest
v,p=input,print;k,m,l,c,s=v().count(' '),int(v()),[],0,1;n=[v()for i in' '*m];z=m>>1;p(m-z)
while n:c,m,s=(c+k)%m,~-m,s^1;w=n.pop(c);[(l:=l+[w])if s else p(w)]
p(z,*l,sep='\n')

# One-line:
# v,p=input,print;k,m,l,c,s=v().count(' '),int(v()),[],0,1;n=[v()for i in' '*m];z=m>>1;p(m-z);exec('while n:c,m,s=(c+k)%m,~-m,s^1;w=n.pop(c);[(l:=l+[w])if s else p(w)]');p(z,*l,sep='\n')

# Original
# num_key = len(input().split())-1
# num_mem=int(input())
# names = [input()for i in range(num_mem)]
# l1 = []
# curr = 0
# print((num_mem+1)//2)
# while names:
#     curr=(curr+num_key)%num_mem
#     print(names.pop(curr))
#     num_mem-=1
#     if not names:break
#     curr=(curr+num_key)%num_mem
#     l1.append(names.pop(curr))
#     num_mem-=1
# print(len(l1))
# print(*l1,sep='\n')

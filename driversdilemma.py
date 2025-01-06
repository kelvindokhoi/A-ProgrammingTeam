# driversdilemma

f=float;C,R,D=map(f,input().split());a=0;exec('m,g=map(f,input().split());a=m*(C/2-R*D/m-D/g>0)or a;'*6)
print(f"YES {int(a)}"if a else"NO")
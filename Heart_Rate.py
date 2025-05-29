# Heart_Rate.py


# heartrate
# https://open.kattis.com/problems/heartrate

# python Heart_Rate.py < Heart_Rate_in.txt


for _ in[0]*int(input()):
   b,p=map(float,input().split())
   print(60*(b-1)/p,60*b/p,60*(b+1)/p)


# golfed:
# for l in[*open(0)][1:]:b,p=map(float,l.split());a=60/p;b*=a;print(b-a,b,b+a)
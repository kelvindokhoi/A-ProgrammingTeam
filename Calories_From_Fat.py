# Calories_From_Fat.py


# calories
# https://open.kattis.com/problems/calories

# python Calories_From_Fat.py < Calories_From_Fat_in.txt

# the gram + the calories = 100% - the percentages => use to find the total calories

from collections import defaultdict
import sys

tracking = defaultdict(list)
for name in ['fat','protein','sugar','starch','alcohol']:tracking[name] = [0,0]
final_fat = 0
final_calories = 0
conversion = {'fat':9,'protein':4,'sugar':4,'starch':4,'alcohol':7}
data = False

def Adding_Elements(line:str,tracking:defaultdict):
    for item,name in zip(map(str,line.rstrip().split()),['fat','protein','sugar','starch','alcohol']):
        num,unit = float(item[:-1]),item[-1]
        if unit == 'g':
            tracking[name][0] += num*conversion[name]
        elif unit == 'C':
            tracking[name][0] += num
        else:
            tracking[name][1] += num/100

for line in sys.stdin:
    if line.rstrip() != '-':
        Adding_Elements(line,tracking)
        data = True
        calories = 0
        percent = 0
        result = list(tracking.values())
        for item in result:
            calories += item[0]
            percent += item[1]
        total_calories = calories/(1-percent) if percent!=0 else calories
        final_fat += (tracking['fat'][0]+tracking['fat'][1]*total_calories)
        final_calories += total_calories
        for name in ['fat','protein','sugar','starch','alcohol']:tracking[name] = [0,0]
    else:
        if data:
            print(f"{round(final_fat/final_calories*100,None)}%")
            final_fat = 0
            final_calories = 0
            data = False

# golfed:
# c=[9,4,4,4,7];F=C=0;import sys
# for l in sys.stdin:
#  if l[0]!="-":
#   s=l.split();t=p=0
#   for i,x in enumerate(s):
#    n,u=int(x[:-1]),x[-1]
#    if u=="%":p+=n/100
#    else:t+=(n:=[n*c[i],n][u=='C'])
#    if i==0:f,s=n,u
#   t/=1-p;F+=f*[1,t/100][s=='%'];C+=t
#  elif C:print(f"{F/C*100:.0f}%");F=C=0
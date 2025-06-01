# Beat_the_Spread.py


# beatspread
# https://open.kattis.com/problems/beatspread

# python Beat_the_Spread.py < Beat_the_Spread_in.txt

for l in[*open(0)][1:]:
    a,b=map(int,l.split())
    c,d=(a+b)//2,(a-b)//2
    if c<0 or d<0 or c+d!=a or c-d!=b:
        print('impossible')
    else:print(c,d)
# lineup
# Line Them Up

# a=[input()for i in' '*int(input())];b=sorted(a);print("DECREASING"if a==b[::-1]else["NEITHER","INCREASING"][a==b])
# b=sorted(a:=[input()for i in' '*int(input())]);print("DECREASING"if a==b[::-1]else["NEITHER","INCREASING"][a==b])
# a=[*open(0)][1:];print(('NEITHER','INCREASING')[a==sorted(a)]if a!=sorted(a)[::-1]else'DECREASING')
b=sorted(a:=[*open(0)][1:]);print(('NEITHER','INCREASING')[a==b]if a!=b[::-1]else'DECREASING')

# a=[input()for i in' '*int(input())];b=sorted(a);print("DECREASING"if a==b[::-1]else["NEITHER","INCREASING"][a==b])
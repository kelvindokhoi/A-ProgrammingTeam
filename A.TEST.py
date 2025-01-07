# i,j=int,input;x={i(j())for m in' '*~-i(j())}
# c=sorted({*range(1,i(j()))}-x)
# print(*(c or['good job']),sep='\n')

*a,=map(int,open(0).read().split())
b={*range(1,-~a[-1])}-{*a[1::]}
print(*(b or['good job']),sep='\n')

a=[*map(int,open(0))];print(*({*range(1,-~a[-1])}-{*a[1:]}or['good job']),sep='\n')

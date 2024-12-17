# planina

# explain:
# the number of squares in one edge is calculated using the iritation (call i): 2^i
# the number of points in the middle is calculated using the number of squares (call x): (x-1)^2
# the number of points on the outside is calculated using the number of squares (call x): (x+1)*2+(x-1)*2 = 4x

# i=int(input());print(4*(x:=2**i)+(x-1)**2)
# after simplifiedcation:

print((2**int(input())+1)**2)
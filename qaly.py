# qaly
# Quality-Adjusted Life-Year

sumz = 0
for i in range(int(input())):
    no1,no2 = map(float,input().split())
    sumz = sumz + no1*no2
print(f"{sumz:.3f}")
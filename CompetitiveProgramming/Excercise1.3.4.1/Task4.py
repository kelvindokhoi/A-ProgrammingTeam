#print out unique sorted numbers

inplist = []

while n:=input():
    inplist.append(int(n))

print(*(set(inplist)).sort(),sep="\n")

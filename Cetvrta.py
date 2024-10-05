def retVector(a,b,c):
    retX = 0
    retY = 0
    if a[0] != b[0] and a[0]!= c[0]:
        retX = a[0]
    elif b[0]!= a[0]:
        retX = b[0]
    else:
        retX = c[0]
    if a[1] != b[1] and a[1] != c[1]:
        retY = a[1]
    elif b[1]!= a[1]:
        retY = b[1]
    else:
        retY = c[1]
    return str(retX)+" "+str(retY)

def main():
    pointA = [int(x) for x in input().split(" ")]
    pointB = [int(x) for x in input().split(" ")]
    pointC = [int(x) for x in input().split(" ")]
    print(retVector(pointA,pointB,pointC))

if __name__ == "__main__":
    main()
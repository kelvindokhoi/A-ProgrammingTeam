friends, days, today = map(int, input().split(" "))

def quarantine(start):
    end = start + 14
    if end>(today+days):
        return False
    else:
        return True
    
def main():
    n = 0
    for _ in range(friends):
        if quarantine(int(input())):
            n+=1
    print(n)

if __name__ == "__main__":
    main()
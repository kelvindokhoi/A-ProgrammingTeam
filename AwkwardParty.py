#try to use dict nd dict.keys to solve the indexing

def location(individual, array):
    locList = [i for i, value in enumerate(array) if value == individual]
    if len(locList) < 2:
        return float('inf')
    return min(locList[i+1] - locList[i] for i in range(len(locList) - 1))

def main():
    minimum = float("inf")
    people = int(input())
    arrPeople = [int(i) for i in input().split(" ")]
    existed = []
    existed = [a for a in range(people) if a not in existed]
    minimum = min(location(existed[i], arrPeople) for i in range(len(existed)))
    if minimum != float("inf"):
        print(minimum)
    else:
        print(people)

if __name__ == "__main__":
    main()
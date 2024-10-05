def countVowels(word):
    count = 0
    for i in range(len(word)-1):
        if word[i] in 'aeiouy' and word[i]==word[i+1]:
            count += 1
    return count

def main():
    answer = []
    while True:
        totalCase = int(input())
        if totalCase == 0:
            break
        mapper = [input() for _ in range(totalCase)]
        mapper.sort(reverse=True,key=countVowels)
        answer.append(mapper[0])
    for i in range(len(answer)):
        print(answer[i])

if __name__ == '__main__':
    main()

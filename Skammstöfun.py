def FirstLetter(word):
    if word[0].isupper():
        return True
def main():
    totalWords = int(input())
    result = ""
    listWords = [x for x in input().split(" ")]
    for i in range(totalWords):
        if FirstLetter(listWords[i]):
            result += listWords[i][0]
    print(result)

if __name__ == '__main__':
    main()
ii = int(input())
answer = []

def unmeme(string):
    result = string.lower()
    result = list(result)
    result[0] = result[0].upper()
    return "".join(str(n) for n in result)


for i in range(ii):
    wordmap = input()
    answer.append(unmeme(wordmap))
for j in range(ii):
    print(answer[j])
    
# alphabetanimals.py
# Alphabet Animals
# python alphabetanimals.py <

prev_word = input()
word_li = [input()for _ in' '*int(input())]
word_dict = dict()
for i,word in enumerate(word_li):
    if word[0] not in word_dict:
        word_dict[word[0]]={(i,word)}
    else:
        word_dict[word[0]].add((i,word))
last_c = prev_word[-1]
if last_c not in word_dict:
    print("?")
else:
    found = False
    for _,w in word_dict[last_c]:
        if w[-1] not in word_dict or (w[0]==w[-1] and len(word_dict[last_c])==1):
            print(w+'!')
            found = True
            break
    if not found:
        print(sorted(list(word_dict[last_c]))[0][1])

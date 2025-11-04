# addemup
# https://open.kattis.com/problems/addemup
from collections import defaultdict

num_cards, desired_num = map(int,input().split())
cards = list(input().split())

def find_reverse():
    num_dict = {'1':'1','2':'2','5':'5','6':'9','9':'6','8':'8','0':'0'}
    def reverse_num(num):
        reversible = True
        new_num = []
        for char in num[::-1]:
            if char in num_dict:
                new_num.append(num_dict[char])
            else:
                reversible = False
                break
        if reversible:
            return ''.join(new_num)
        else:
            return ''
    return reverse_num

reverse_num = find_reverse()
counter_for_repeats = defaultdict(lambda:0)

concatible = dict()
for card in cards:
    counter_for_repeats[int(card)]+=1
    concatible[int(card)] = card

    alt_card = reverse_num(card)
    if alt_card!='' and alt_card!=card:
        counter_for_repeats[int(alt_card)]+=1
        concatible[int(alt_card)] = alt_card
        


possible_cards = set()
matches = set()
for card in counter_for_repeats.keys():
    icard = int(card)
    target = desired_num-icard
    if target>=0:
        if card in possible_cards:
            matches.add((icard,target))
        possible_cards.add(target)

found = False
for start,end in matches:
    s_start = concatible[start]
    s_end = concatible[end]
    if reverse_num(s_end)==s_start:
        if counter_for_repeats[end]>=2:
            found = True
            break
    else:
        # print(reverse_num(str(start)),end)
        found = True
        break
print('YES'if found else 'NO')
# print(counter_for_repeats)
# print(concatible)
# print(matches)
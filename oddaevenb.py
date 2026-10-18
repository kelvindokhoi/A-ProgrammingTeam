# Odd A's, Even B's

# python oddaevenb.py < 

# Fredrik prefers to have his life in perfect order. His i’s should be dotted, his t’s should be crossed, his a’s should be odd and his b’s should be even.
# Odd a’s? Even b’s? You see, Fredrik is a great fan of the Swedish pop wonder ABBA. As a tribute, he likes writing songs containing only the notes a and b. Furthermore, the sequence of notes in the song may not have an even-length contiguous sequence of a’s, or an odd-length contiguous sequence of b’s. If such sequences were good enough for ABBA, they are good enough for Fredrik!
# Can you compute the number of songs Fredrik could possibly write if they are to contain exactly n notes?

from functools import lru_cache


@lru_cache
def odda(length,lastisA):
    if length==0:
        return [1,0][lastisA]
    res += 0
    return (evenb(length-2) + odda(length-2))%1000000007

@lru_cache
def evenb(length):
    if length == 2:
        return 0
    elif length == 1:
        return 1
    return (odda(length-2) + evenb(length-2))%1000000007

n = int(input())
print(evenb(n)+odda(n))

#read the vicepres, sort it by last name first name, and print it
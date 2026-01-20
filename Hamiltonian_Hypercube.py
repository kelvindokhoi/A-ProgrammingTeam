# Hamiltonian Hypercube
# https://open.kattis.com/problems/hypercube

#000, 001, 011, 010, 110, 111, 101, 100

# 0,1
# 00, 01, 11, 10
def flip(key):
    new_key = ''
    for char in key:
        if char=='1':
            new_key += '0'
        else:
            new_key += '1'
    return new_key

def position_of(key):
    if len(key)==0:
        return 0
    else:
        if key[0]=='0':
            return position_of(key[1:])
        else:
            # print(key,key[-1:0:-1])
            return 2**(len(key)) - 1 - position_of(key[1::])

def main():
    dimension, a, b = input().split()
    print(abs(position_of(b)-position_of(a))-1)

def test():
    all_entries = [*"000, 001, 011, 010, 110, 111, 101, 100".split(sep=', ')]

    for entry in all_entries:
        print(entry,position_of(entry))

# test()
main()

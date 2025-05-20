from random import randint

def create_random_hex(num_char):
    hex_num = '0x'
    for i in range(num_char):
        hex_num+=hex(randint(0,15))[2]
    return int(hex_num,16)

def checkans(answer,reply):
    return answer==reply
num1 = create_random_hex(4)
num2 = create_random_hex(4)
plus = hex(num1+num2)
while int(plus,16)>=int('0x10000',16):
    num1 = create_random_hex(4)
    num2 = create_random_hex(4)
    plus = hex(num1+num2)
minus = hex(num1-num2)

print(f'Adding {hex(num1)} and {hex(num2)}.')
while input('Your answer is: ')!=plus:
    print('Try again.')
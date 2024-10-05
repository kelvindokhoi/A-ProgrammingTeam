def convert_to_bin(num):
    return bin(num)[2:]
def revert_bin(bin_num):
    return int(bin_num[::-1], 2)

number = int(input())
print(revert_bin(convert_to_bin(number)))
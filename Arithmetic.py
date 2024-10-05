#Arithmetic

dict8 = {"0":"000",
         "1":"001",
         "2":"010",
         "3":"011",
         "4":"100",
         "5":"101",
         "6":"110",
         "7":"111"}
dict16 = {
    "0000": "0",
    "0001": "1",
    "0010": "2",
    "0011": "3",
    "0100": "4",
    "0101": "5",
    "0110": "6",
    "0111": "7",
    "1000": "8",
    "1001": "9",
    "1010": "A",
    "1011": "B",
    "1100": "C",
    "1101": "D",
    "1110": "E",
    "1111": "F"
}

def base8to2(base8):
    base2 = ''.join(dict8[digit] for digit in base8)
    padding = (4 - len(base2) % 4) % 4
    return '0' * padding + base2

def base2to16(base2):
    result = ''.join(dict16[base2[i]+base2[i+1]+base2[i+2]+base2[i+3]] for i in range(0, len(base2)-3, 4))
    result = result.lstrip("0")
    print(result)

def main():
    inputt = input()
    if inputt == "0":
        print(0)
    else:
        base2 = base8to2(inputt)
        base2to16(base2)

if __name__ == "__main__":
    main()
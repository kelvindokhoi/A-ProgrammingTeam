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

def base2to16(base2):
    length = len(base2)
    result = ""
    for i in range(0,length-3,4):
        print(i)
        temp4 = base2[i]+base2[i+1]+base2[i+2]+base2[i+3]
        result += dict16[temp4]
    print(result)

base2to16(input())
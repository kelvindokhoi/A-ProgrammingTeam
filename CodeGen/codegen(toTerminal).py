# There is a VScode Terminal bug that occasionally prints out an extra "]"
#there is a coding bug that skips the \n
# Your code here
my_code="""print("Hellooooooo Worldddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd!")"""

def Golf(code):
    code=code.encode('unicode_escape').decode('u8') #to avoid missing escape marked things like \n,\a,\t...
    if len(code) % 2 != 0:  #make the code even
        code += " "
    return "".join([code[i:i+2].encode('u8').decode('utf-16') for i in range(0,len(code),2)])

print(f"exec(bytes('{Golf(my_code)}','u16')[2:])")


# There is a VScode Terminal bug that occasionally prints out an extra "]"
# Your code here
my_code="""print("Hello World")"""

def Golf(code):
    if len(code) % 2 != 0:
        code += " "
    return "".join([code[i:i+2].encode('utf-8').decode('utf-16') for i in range(0,len(code),2)])

print(f"exec(bytes('{Golf(my_code)}','u16')[2:])")


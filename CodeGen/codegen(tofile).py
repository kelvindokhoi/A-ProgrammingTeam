import os

code="""a=int(input());b=input()
for i in range(a,1,-1):
    print(f"{i} bottles of {b} on the wall, {i} bottles of {b}.\nTake one down, pass it around, {i-1} bottle{'s'if i-2 else''} of {b} on the wall.\n")
print(f"1 bottle of {b} on the wall, 1 bottle of {b}.\nTake it down, pass it around, no more bottles of {b}.")"""

def get_absolute_path(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, filename)

def write_to_file(output_data):
    filename=get_absolute_path("output.py")
    with open(filename, mode="w",encoding='utf-8') as f:
        f.write(output_data)

def Golf(code):
    code=code.encode('unicode_escape').decode('u8') #to avoid missing escape marked things like \n,\a,\t...
    if len(code) % 2 != 0:  #make the code even
        code += " "
    return "".join([code[i:i+2].encode('u8').decode('utf-16') for i in range(0,len(code),2)])

code=Golf(code)

write_to_file("exec(bytes('"+code+"','u16')[2:])")
print(f"exec(bytes('{code}','u16')[2:])")
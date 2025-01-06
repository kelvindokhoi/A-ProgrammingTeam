import os

def get_absolute_path(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, filename)

def write_to_file(output_data):
    filename=get_absolute_path("output.txt")
    with open(filename, mode="w",encoding='utf-16') as f:
        f.write(output_data)

def Golf(code):
    if len(code) % 2 != 0:
        code += " "
    return "".join([code[i:i+2].encode('utf-8').decode('utf-16') for i in range(0,len(code),2)])

code="""participants,budget,hotels,weeks=map(int,input().split())
minPrice=1e7
for i in range(hotels):
    price=int(input())
    beds=[*map(int,input().split())]
    for j in range(weeks):
        if beds[j]>=participants:
            if price<minPrice:
                minPrice=price
ans=minPrice*participants
print(ans if ans<budget else 'stay home')"""

write_to_file("exec(bytes('"+Golf(code)+"','u16')[2:])")
import os

code="""def D(y):w=sum(D(a)for a in t[y]);r=m[y]-1;w+=abs(r);m[y]=1;m[p[y]]+=r if p[y]!=-1 else 0;return w
while(n:=int(input())):
 t,m,p,l=[[]for _ in' '*n],[0]*n,[-1]*n,range
 exec('v,q,_,*c=map(int,input().split());v-=1;c=[x-1 for x in c];t[v]=c;m[v]=q\nfor x in c:p[x]=v\n'*n)
 print(D([x for x in l(n)if p[x]<0][0]))"""

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
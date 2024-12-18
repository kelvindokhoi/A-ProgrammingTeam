# onechicken
# One Chicken Per Person!

a,b = map(int,input().split())
if abs(a-b)-1:
    print(f"Dr. Chaz will have {b-a} pieces of chicken left over!" if a<b else f"Dr. Chaz needs {a-b} more pieces of chicken!")
else:
    print(f"Dr. Chaz will have {b-a} piece of chicken left over!" if a<b else f"Dr. Chaz needs {a-b} more piece of chicken!")
# iBoard
# python iBoard.py < iBoard.txt

while True:
    try:
        nums = {'0':0,'1':0}
        num = ''.join(format(ord(i),'07b')for i in input())
        for c in num:
            nums[c]+=1
        print('trapped'if nums['0']&1 or nums['1']&1 else'free')
    except EOFError:break
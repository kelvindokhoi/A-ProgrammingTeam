totalCon = eval(input())
oneGroup = totalCon // 4

nAns = (oneGroup-1)*(oneGroup*2)+4

print(nAns)


#ans = list(format(nAns,".0f"))

'''
if eval(ans[len(ans)-1]) >= 6:
    ans[len(ans)-1] = str((eval(ans[len(ans)-1])+4)%10)
    ans[len(ans)-2] = str((eval(ans[len(ans)-1])+4)//10)
else:
    ans[len(ans)-1] = str((eval(ans[len(ans)-1])+4))

new_string = "".join(ans)
print(new_string)
'''

'''
# Convert num to string
def convertNtoS(num):
    output = ""
    while num != 0:
        currEx = 0
        while num > currEx:
            if currEx==0:
                currEx += 10
            else:
                currEx *= 10
        output += str(int(num // (currEx/10)))
        num -= (num // (currEx/10)) * (currEx/10)
    return output

outp = convertNtoS(ans)

print(outp)
'''

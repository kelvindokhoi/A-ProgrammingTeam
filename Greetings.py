def identify(string):
    length = len(string)
    e = 0
    notHey = False
    notLater = True
    if string[0] == "h" and string[length-1] == "y":
        for i in range(1,length-1):
            if string[i]=="e":
                e+=1
            else:
                    notHey = True
                    break
    else:
        notHey = True
    if string == "Later!":
        noteLater = False
    if not(notHey):
        return "h"+"e"*2*e+"y"
    if notLater:
        return "Alligator!"

def main():
    stringHere = input()
    print(identify(stringHere))

if __name__ == "__main__":
    main()
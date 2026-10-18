# GlitchBot

# python GlitchBot.py < GlitchBot_in.txt
botx,boty = map(int,input().split())

num_I = int(input())
bot_dir = 0
dir_li = [(1,0),(0,1),(-1,0),(0,-1)]
cmdli = []
all_possible_ins = {"Forward","Right","Left"}
for i in range(num_I):
    ins = input()
    if ins=="Forward":
        x,y = dir_li[bot_dir]
        botx += x
        boty += y
    elif ins=="Right":
        bot_dir = (bot_dir+1)%4
    else:
        bot_dir = (bot_dir-1)%4
    cmdli.append((ins,bot_dir,botx,boty))
for i in range(num_I):
    ins = cmdli[i][0]
    other_ins = all_possible_ins-{ins}
    for o_ins in other_ins:
        ins,bot_dir,botx,boty = cmdli[i]
        if o_ins=="Forward":
            x,y = dir_li[bot_dir]
            botx += x
            boty += y
        elif o_ins=="Right":
            bot_dir = (bot_dir+1)%4
        else:
            bot_dir = (bot_dir-1)%4
        for j in range(i+1,num_I):
            ins = cmdli[j][0]
            if ins=="Forward":
                x,y = dir_li[bot_dir]
                botx += x
                boty += y
            elif o_ins=="Right":
                bot_dir = (bot_dir+1)%4
            else:
                bot_dir = (bot_dir-1)%4
        print(botx,boty)
        if botx==0 and boty==0:
            print(i+1,o_ins)
            break
# Guessing Game
# python Guessing_Game.py < Guessing_Game_in.txt > Guessing_Game_out.txt

upper = 10
lower = 1
lying = False
def reset():
    global upper
    global lower
    global lying
    upper = 10
    lower = 1
    lying = False

while True:
    try:
        number = int(input())
        response = input()
        if upper==lower==number and response!='right on':
            lying = True
        if response=='too high':
            if number<=lower:
                lying = True
            else:
                upper = min(number-1,upper)
        elif response=='too low':
            if number>=upper:
                lying = True
            else:
                lower = max(number+1,lower)
        if response == 'right on':
            if lower<=number<=upper and (not lying) and upper>=lower:
                print("Stan may be honest")
            else:
                print("Stan is dishonest")
            reset()
    except EOFError:
        break
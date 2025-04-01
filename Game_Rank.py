# Game Rank
# gamerank

# Rank 25-21: 2 stars
# Rank 20-16: 3 stars
# Rank 15-11: 4 stars 
# Rank 10-1: 5 stars

# If player rank 6-25 have 3 consecutive wins, gain +1 star 
# If player on rank 1-20 lose a game, they lose 1 star
# Legend will always be legend.

# python Game_Rank.py < game_rank_in.txt > game_rank_out.txt

class Player:
    def __init__(self):
        self.rank = 25
        self.star = 0
        self.consec = 0
    def __repr__(self):
        return f"Rank: {self.rank}, Star: {self.star}, Streak: {self.consec}"
    def returnstar(self):
        if 21<=self.rank<=25:
            return 2
        elif 16<=self.rank<=20:
            return 3
        elif 11<=self.rank<=15:
            return 4
        elif 1<=self.rank<=10:
            return 5
        else:
            return 0
    def win(self):
        self.consec+=1
        self.star += 2 if (self.consec>=3 and 6<=self.rank<=25) else 1
        if self.star>self.returnstar() and self.rank>0:
            self.star = self.star-self.returnstar()
            self.rank-=1
    def lose(self):
        self.consec = 0
        if self.star <= 0 and self.rank>0 and self.rank<20:
            self.rank += 1
            self.star = self.returnstar() - 1
        else:
            self.star -= 0 if (self.rank>20 or self.rank==0 or (self.rank==20 and self.star==0)) else 1
    def calculate_rank(self,state):
        if state=='W':
            self.win()
        elif state=='L':
            self.lose()
        else:
            pass

# while True:
#     try:
#         my_Player = Player()
#         for c in input():
#             my_Player.calculate_rank(c)
#             print(c,my_Player.__repr__())
#         print('Legend'if my_Player.rank==0 else my_Player.rank)
#     except EOFError:break

my_Player = Player()
for c in input():
    my_Player.calculate_rank(c)
    # print(c,my_Player.__repr__())
print('Legend'if my_Player.rank==0 else my_Player.rank)
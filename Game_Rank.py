# Game Rank
# gamerank

# Rank 25-21: 2 stars
# Rank 20-16: 3 stars
# Rank 15-11: 4 stars 
# Rank 10-1: 5 stars

# If player rank 6-25 have 3 consecutive wins, gain +1 star 
# If player on rank 1-20 lose a game, they lose 1 star
# Legend will always be legend.

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
    def promote(self):
        self.rank -= 1
        self.star = 0
    def demote(self):
        self.rank += 1
        self.star = self.returnstar() - 1
    def win(self):
        self.consec+=1
        for _ in range(2 if self.consec>=3 and 6<=self.rank<=25 else 1):
            self.star += 1
            if self.star>=self.returnstar():
                self.promote()
    def lose(self):
        self.consec = 0
        if 20<self.rank or self.rank==0:
            pass
        else:
            if self.star == 0:
                self.demote()
            else:
                self.star -= 1
    def calculate_rank(self,state):
        if state=='W':
            self.win()
        else:
            self.lose()


my_Player = Player()
for c in input():
    my_Player.calculate_rank(c)
    print(c,my_Player.__repr__())
print('Legend'if my_Player.rank==0 else my_Player.rank)
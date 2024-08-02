import random

class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)


class Game:
    def __init__(self, Dice):
        self.Dice = Dice
    
    def play(self):
        total=0
        for die in self.Dice:
            total =+ die.roll()
        return total

class Bet:
    def __init__(self, Game):
        self.Game = Game

    def bet(self, amount, number, guess):
        
        # To do: Add real odds to the bet
        odds = 2
        
        if guess == 'over':
            if self.Game.play() > number:
                return amount*odds
            else:
                return 0
        elif guess == 'under':
            if self.Game.play() < number:
                return amount*odds
            else:
                return 0
        else:
            if self.Game.play() == number:
                return amount*odds


dice = Dice(6)
dice_list = [dice]
game = Game(dice_list)
bet = Bet(game)


print(bet.bet(10, 3, 'over'))
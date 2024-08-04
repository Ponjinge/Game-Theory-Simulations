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
            total += die.roll()
        return total

class Player:
    def __init__(self, balance):
        self.balance = balance

    def __bet__(self, Game, amount, number, guess):
        
        # To do: Add real odds to the bet
        odds = 2
        
        if guess == 'over':
            if Game.play() > number:
                return amount*odds
            else:
                return 0
        elif guess == 'under':
            if Game.play() < number:
                return amount*odds
            else:
                return 0
        else:
            if Game.play() == number:
                return amount*odds
    
    def place_bet(self, Game, amount, number, guess):
        self.balance -= amount
        self.balance += self.__bet__(Game, amount, number, guess)
        return self.balance

#Main

dice6 = Dice(6)
dice10 = Dice(10)
dice_list = [dice6, dice10]
game = Game(dice_list)
player = Player(100)

for i in range(1000):
    player.place_bet(game, player.balance*0.50, 7, 'over')
    print(player.balance)




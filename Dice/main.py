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
        if amount <= self.balance:
            self.balance -= amount
            self.balance += self.__bet__(Game, amount, number, guess)
        else:
            pass
            #print('Insufficient funds')
        return self.balance

#Main

dice6 = Dice(6)
dice10 = Dice(10)
dice_list = [dice6]
game = Game(dice_list)
player = Player(100)


# Test Strategy
# k=0.01
# for i in range(1000):
#     prevbalance = player.balance
#     player.place_bet(game, player.balance*k, 3, 'over')
#     if player.balance < prevbalance:
#         k=k*2
#     else:
#         k=0.01
#     print(player.balance)
    

# Martingale Strategy
successes = []
for k in range(1000):
    print(f'\r{k} out of 1000', end='')
    success = 0
    for j in range(1000):
        player = Player(k)
        bet_amount = 1
        for i in range(100):
            prevbalance = player.balance
            player.place_bet(game, bet_amount, 3, 'over')
            if player.balance < prevbalance:
                bet_amount = bet_amount*2
            else:
                bet_amount = 1
        #print(player.balance)
        if player.balance > 100:
            success += 1
    #print(f'There were {success} successful runs out of 1000')
    successes.append(success)

import matplotlib.pyplot as plt
plt.plot(successes)
plt.savefig('successes.png')
#Combinatorics and Probability

import statistics
import prisoner_dilemma
from players.red import Red 
from players.green import Green 
from players.tit_for_tat import TitForTat
from players.nasty import Nasty

        
G = Green()
R = Red()
T4T = TitForTat()
N = Nasty()

player_list = [G,R,T4T,N]

# Single game test
print(prisoner_dilemma.game(G,R,10)) # expected output: [0, 50]

# Single game test with algorithms that use previous choices to make a decision
print(prisoner_dilemma.game(T4T, N, 10))

# Test one set of 100 rounds between all players
print(prisoner_dilemma.p_set(player_list, 100))

# Test a simple tournament
prisoner_dilemma.tournament(player_list, 5, 250)

print(prisoner_dilemma.evolvelist(player_list, 250, 3, 4, 'top_bottom', 2))



print(G)
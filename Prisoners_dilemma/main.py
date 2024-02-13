import statistics
#from evolution_model import evolvelist
from players.red import Red 
from players.green import Green 
from players.tit_for_tat import TitForTat
from players.nasty import Nasty

def game(Player1, Player2, rounds):
    previous_rounds = []
    totalscore = [0,0]
    for _ in range(rounds):
        player1_choice = Player1.decide(previous_rounds, 0)
        player2_choice = Player2.decide(previous_rounds, 1)
        previous_rounds.append((player1_choice, player2_choice))
        scores = prisoners_dilemma(player1_choice, player2_choice)
        totalscore[0] += scores[0]
        totalscore[1] += scores[1] 
    return totalscore

    
        
def p_set(player_list, rounds):
    
    # Setup the scoring
    set_scores = []
    for i in range(len(player_list)):
        set_scores.append(0)
        
    # Each player goes head to head with every other player once    
    for i in range(len(player_list)):
        for j in range(i, len(player_list)):
            game_score = game(player_list[i], player_list[j], rounds)
            set_scores[i] += game_score[0]
            set_scores[j] += game_score[1]
            
    #Return the cumulative scores for the set
    return set_scores


def tournament(player_list, num_sets, num_rounds):
        for _ in range(num_sets):
            print(p_set(player_list, num_rounds))

def prisoners_dilemma(first_player_choice, second_player_choice):
    outcome = (first_player_choice, second_player_choice)
    match outcome:
        case (0,1):
            return (0,5)
        case(1,0):
            return (5,0)
        case(0,0):
            return (3,3)
        case(1,1):
            return (1,1)

        case _ :
            return (0,0)
        
G = Green()
R = Red()
T4T = TitForTat()
N = Nasty()

player_list = [G,R,T4T,N]

# Single game test
print(game(G,R,10)) # expected output: [0, 50]

# Single game test with algorithms that use previous choices to make a decision
print(game(T4T, N, 10))

# Test one set of 100 rounds between all players
print(p_set(player_list, 100))

# Test a simple tournament
tournament(player_list, 5, 250)


def evolvelist(player_list, rounds, pool_size, generations):
    for _ in range(pool_size):
        player_list += player_list 
        
    for _ in range(generations):
        set_scores = p_set(player_list, rounds)
        previous_players = set()
        for i in range(len(player_list )- 1, -1, -1):
            if player_list[i] not in previous_players:
                previous_players.add(player_list[i])
                if set_scores[i] < statistics.median(set_scores):
                    player_list.pop(i)
                else:
                    player_list.append(player_list[i])
    



evolvelist(player_list, 250, 3, 50)
print(player_list)
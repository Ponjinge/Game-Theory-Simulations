import statistics

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

def prisoners_dilemma(first_player_choice, second_player_choice, coop_score=3, steal_score=5, victim_score=0, both_betray_score=1 ):
    outcome = (first_player_choice, second_player_choice)
    match outcome:
        case (0,1):
            return (victim_score,steal_score)
        case(1,0):
            return (steal_score,victim_score)
        case(0,0):
            return (coop_score,coop_score)
        case(1,1):
            return (both_betray_score,both_betray_score)

        case _ :
            return (0,0)


def evolvelist(player_list, rounds=50, pool_size=3, generations=10, mutating='mean', cull = 3):
    for _ in range(pool_size):
        player_list += player_list 
        
    for _ in range(generations):
        print(len(player_list))
        #print(player_list)
        set_scores = p_set(player_list, rounds)
        previous_players = set()
        match mutating:
            case 'mean' :    
                for i in range(len(player_list )- 1, -1, -1):
                    if player_list[i] not in previous_players:
                        previous_players.add(player_list[i])
                        if set_scores[i] < statistics.median(set_scores):
                            player_list.pop(i)
                        else:
                            player_list.append(player_list[i])
                            
            case 'top_bottom':            
                k=0
                max_bred = False
                for _ in range(cull):
                    for i in range(len(player_list )- 1, -1, -1):
                        if player_list[i] not in previous_players:
                            previous_players.add(player_list[i])
                            
                            if set_scores[i] == min(set_scores):
                                player_list.pop(i)
                                k +=1
                            
                            elif max_bred==False and set_scores[i] == max(set_scores):
                                for _ in range(cull):
                                    player_list.append(player_list[i])
                                max_bred = True
                                
        # Check if all elements are the same
        if all(x == player_list[0] for x in player_list) == True: 
            print("One player has taken over the gene pool")
            return player_list
        
    return player_list


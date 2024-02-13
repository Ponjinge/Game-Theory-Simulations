
import statistics

#from main import p_set

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
    






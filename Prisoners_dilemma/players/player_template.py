class ClassName:
    def __init__(self):
        pass
    
    def __str__(self):
        return self.__class__.__name__
    
    def __repr__(self):
        return self.__class__.__name__

    

    # All players must have this method
    def decide(self, previous_choices = [], position = 0):
        
        # Position indicates whether you are the first or second player
        # This is used for determining what your or your opponent's last move was
        
        if position == 0:
            k = 1 #Opponent pos
        else:
            k = 0 #Opponent pos
        
        # If first round
        if previous_choices == []:
            return 1 # Defect
        
        # If you cooperated last time
        if previous_choices[-1][position] == 0 :
            return 0 # Cooperate
        
        # If your opponent defected last time
        elif previous_choices[-1][k] == 0:
            
            return 0 # Cooperate
        
        else:
            return 1 # Defect
        
        
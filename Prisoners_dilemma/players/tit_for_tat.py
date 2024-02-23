class TitForTat:
    def __init__(self):
        pass

    
    def __str__(self):
        return self.__class__.__name__
    
    def __repr__(self):
        return self.__class__.__name__

    
    def decide(self, previous_choices = [], position = 0):
        
        #Determine what the opponent did last time
        if position == 0:
            k = 1
        else:
            k = 0
            
        # Cooperate if it is the first round    
        if previous_choices == []:
            return 0
        
        # Defect if the opponent defected last time
        elif previous_choices[-1][k] == 1:
            return 1
        
        # Cooperate if the opponent cooperated last time
        else:
            return 0
class Nasty:
    def __init__(self):
        pass
    def decide(self, previous_choices = [], position = 0):
        
        #Determine what the opponent did last time
        if position == 0:
            k = 1
        else:
            k = 0
            
        # Cooperate for the first two rounds     
        if len(previous_choices)<2:
            return 0
        
        # Defect if the opponent cooperated the previous two times
        elif len(previous_choices)>=2 and previous_choices[-2][k] == 0 and previous_choices[-1][k] == 0:
            return 1
        
        # Cooperate if the opponent cooperated last time
        elif previous_choices[-1][k] == 0:
            return 0
        # Defect if the opponent defected last time
        else:
            return 1
        
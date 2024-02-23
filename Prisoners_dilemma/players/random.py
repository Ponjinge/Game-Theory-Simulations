import random as r

class Random:
    def __init__(self):
        pass
    
    def __str__(self):
        return self.__class__.__name__
    
    def __repr__(self):
        return self.__class__.__name__

    

    # All players must have this method
    def decide(self, previous_choices = [], position = 0):
        
        return r.randint(0,1)
        
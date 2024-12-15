class Game:

    def __init__(self):
        self.current_score = 0  
        self.frame = 1          
        self.throw = 1  
        self.frame_score=0  
        self.rest_pins=15  
        self.bonus=0    

    def calculate_score(self,pd):
        self.frame_score += pd
        self.rest_pins -=pd
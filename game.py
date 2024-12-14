class Game:

    def __init__(self):
        self.current_score = 0  
        self.frame = 1          
        self.throw = 1          

    def calculate_score(self,pd):
        self.current_score += pd
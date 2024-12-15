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
        if self.rest_pins==0 :
            if self.throw==1:
                self.bonus=3
            else :
                self.bonus=2
        if self.throw>=3:
            if self.rest_pins!=0:  
                self.end_frame()
        else :
            self.throw += 1 

    def end_frame(self):
        self.current_score+=self.frame_score
        self.throw = 1  
        self.frame_score=0  
        self.rest_pins=15  
        self.bonus=0
        self.frame +=1
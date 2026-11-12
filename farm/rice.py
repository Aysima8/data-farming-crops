class Rice():
    def __init__(self):
        self.grains = 0
        
    def water(self):
        self.grains += 5
        
    def ripe(self):
        if(self.grains >= 15):
            return True
        else:
            return False
  
    def transplant(self):
        self.grains += 10

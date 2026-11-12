class Corn:
    def __init__(self):
        self.grains = 0
      
    def water(self):
        self.grains +=10
        
    def ripe(self):
        if(self.grains >= 15):
            return True
        else:
            return False

# pylint: disable=too-few-public-methods
class Crop:
    def __init__(self):
        self.grains = 0
        
    def ripe(self):
        if(self.grains >=15 ):
            return True
        else:
            return False
        

from enum import Enum

class Order():
    
    def __init__(self, shipper):
        self._shipper = shipper
        
    @property
    def shipper(self):
        returm self._shipper
        
class Shipper(Enum):
    fedex = 1
    ups = 2
    postal = 3
    
    
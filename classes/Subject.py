import math

class Subject:
    binary = ''
    i = 0
    x = 0
    aptitude = 0

    def __init__(self, i):
        self.i = i
        self.binary = bin(i)[2:]
    
    def set_x(self, a, dx_fit):
        self.x = a +  self.i * dx_fit
        self.set_aptitude()
    
    def set_aptitude(self):
        aux = 0
        if(self.x > 0):
            aux = math.log(abs(self.x**3)) * math.cos(self.x) * math.sin(self.x)
        self.aptitude = aux
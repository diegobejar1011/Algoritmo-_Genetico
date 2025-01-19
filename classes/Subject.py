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
        self.aptitude = 0.1 * self.x * math.log(1 + abs(self.x)) * math.cos(self.x) * math.cos(self.x)


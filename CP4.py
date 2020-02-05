'''
CP4 - Traffic
'''
# modules required for our simulation
import matplotlib.pyplot as plt
import numpy as np

class Traffic(object):
    def __init__(self, myRoadLength, myCarDensity, myIterationNumber):
        # constructor, pulls relevant inputs into the class
        self.RoadLength = myRoadLength
        self.CarDensity = myCarDensity
        self.IterationNumber = myIterationNumber
        
        # creation of road for simulation to take place upon
        self.Road = np.zeros(self.RoadLength)
        
    def update(self):
        # method to update the placement of cars on our road
        self.Road = [0,1,0,0,1,0]
        
        for i in range(0,len(self.Road)):
            print(self.Road)
            try:
                if self.Road[i] == 1:
                    if self.Road[i+1] == 1:
                        self.Road[i] = 1
                    else:
                        self.Road[i] = 0
                        self.Road[i+1] = 1
                elif self.Road[i] == 0:
                    if self.Road[i-1] == 1:
                        self.Road[i] = 1
                    else:
                        self.Road[i] = 0
            except IndexError:
                self.Road[0] == 1
                    
def main():
    t = Traffic(6,1,1)
    t.update()
    
main()
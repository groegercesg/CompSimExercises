'''
CP4 - Traffic
'''
# modules required for our simulation
import matplotlib.pyplot as plt
import numpy as np
import random


class Traffic(object):
    def __init__(self, myRoadLength, myCarDensity, myIterationNumber):
        # constructor, pulls relevant inputs into the class
        self.RoadLength = myRoadLength
        self.CarDensity = myCarDensity
        self.IterationNumber = myIterationNumber

        # creation of road for simulation to take place upon
        self.Road = np.zeros(((self.IterationNumber+1), self.RoadLength))

    def initialise(self):
        # method to initialise the roadway with a certain density of cars in
        # random positions.

        placed_cars = 0
        # counter for number of placed cars so we don't
        # exceed our desired CarDensity
        while placed_cars < int(self.CarDensity*self.RoadLength):
            for i in range(0, self.RoadLength):
                self.Road[0][i] = random.randint(0, 1)
                placed_cars += 1

        return self.Road

    def average_speed(self, car_moves):
        # method to calculate the average speed

        # loop to crawl array to find number of cars
        cars = 0
        for i in range(0, self.RoadLength):
            if self.Road[0][i] == 1:
                cars += 1

        # car_moves passes to method by parameter
        # print average_speed
        try:
            return (car_moves / cars)
        except ZeroDivisionError:
            return 0

    def update(self, init_state):
        # method to update the placement of cars on our road

        self.Road = init_state

        for j in range(0, self.IterationNumber):
            car_moves = 0
            for i in range(0, self.RoadLength):
                if self.Road[j][i] == 1:
                    if self.Road[j][(i+1) % self.RoadLength] == 1:
                        self.Road[j+1][i] = 1
                        # car_moves += 1
                    else:
                        self.Road[j+1][i] = 0
                        # car_moves += 1
                elif self.Road[j][i] == 0:
                    if self.Road[j][(i-1) % self.RoadLength] == 1:
                        self.Road[j+1][i] = 1
                        car_moves += 1
                    else:
                        self.Road[j+1][i] = 0
                        # car_moves += 1
            # average_speeds = average_speeds
            # + " - " + str(car_moves) + " . " +
            # str(self.average_speed(car_moves))
        # return average_speeds
        return self.average_speed(car_moves)

    def simulate(self):
        # method to simulate the traffic junction
        # self.Road = self.initialise()

        print(self.update(self.initialise()))

        # plot of the positions of the cars on the road as a function of time
        plt.imshow(self.Road, interpolation='none', origin='lower')
        plt.show()


'''
def main():
    t = Traffic(20,0.7,25)
    t.simulate()

main()
'''

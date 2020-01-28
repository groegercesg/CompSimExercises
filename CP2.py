'''
CP2 - Decay
'''
# modules required for our simulation
import random
import math

class Decay(object):
    def __init__(self, myLambda, myN, myDelta_t):
        # constructor, pulls in all relevant details to the function
        self.decayCons = myLambda # decay constant
        self.N = myN # length of 2D array
        self.delta_t = myDelta_t # timestep
        
        # create N x N list and set all elements to zero 
        self.Grid = []
        for i in range(0, myN):
            self.Grid.append([])
            for j in range(0, myN):
                self.Grid[i].append(1)
        
    def print_nuclei(self):
        # method to print nuclei, iterates through vertical and horizontal with 
        # two loops, printing line by line
        for i in range(0, len(self.Grid)):
            s = ""
            for j in range(len(self.Grid[i])):
                s += str(self.Grid[i][j]) + " "
            print(s)
        
    def updateN(self):
        # method to update the value of Nuc
        # this crawls the Grid to find the number of undecayed nuclei (1's)
        count_0 = 0
        for i in range(0, self.N):
            for j in range(0, self.N):
                if self.Grid[i][j] == 1:
                    count_0 += 1
        return count_0
    
    def decay_simulation(self):
        # method to simulate the decay of a nuclei
        # creation of variables required for nuclei simulation instance
        p = self.decayCons * self.delta_t # probability that a nucleus decays within a given time period
        hl_sim = 0 # half-life based on simulation, to be incrimented by while loop
        hl_act = round((math.log(2) / self.decayCons), 2)
        Nuc_initial = self.N * self.N # Initial number of undecayed nuclei
        
        # while loop until over half of nucleis have been decayed
        while self.updateN() > int(0.5*Nuc_initial):
            hl_sim += self.delta_t
            # loop through every Grid entry
            for i in range(0, self.N):
                for j in range(0, self.N):
                    if self.Grid[i][j] == 1:
                        # probability for a individual nuclei to decay
                        decay_prob = random.uniform(0,1)
                        '''
                        is this the correct way round?
                        '''
                        if decay_prob < p:
                            self.Grid[i][j] = 0
        
        # decay simulation now over, time to output final values
        print("\n")
        self.print_nuclei()
        print("\n")
        print("Inital number of undecayed nuclei: " + str(Nuc_initial))
        print("Final number of undecayed nuclei: " + str(self.updateN()))
        print("Simulated value of half-life: " + str(hl_sim))
        print("Actual value of half-life: " + str(hl_act))
            
def main():
    # decay constant, length of 2D array, timestep
    '''
    try:
        decaycons = float(input("What is the value of your decay constant: \n"))
        len2D = int(input("What is the length of the 2D array: \n"))
        timestep = float(input("What is the timestep: \n"))
        d = Decay(decaycons, len2D, timestep)
        d.decay_simulation()
    except:
        print("Data entered was not in correct format, please try again!")
        main()
    '''
        
    d = Decay(0.02775,50,0.01)
    d.decay_simulation()

main()

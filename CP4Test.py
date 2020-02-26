from CP4 import Traffic
# modules required for our output
import matplotlib.pyplot as plt
import numpy as np

class TrafficTest(object):
    def run(self):
        t = Traffic(20,0.7,25)
        t.simulate()
        
class SteadyStatePlot(object):
    def run(self):  
        # get input from user about how many incriments we should use
        number_of_incriments = int(input("Number of incriments: \n"))
        # arrays for holding data for x/y axes
        plot_data_x = np.zeros(number_of_incriments)
        plot_data_y = np.zeros(number_of_incriments)
        # interate through all eventualities to get steady-state info for each
        for i in range(0, number_of_incriments):
            t = Traffic(20, (i/number_of_incriments), 50)
            plot_data_x[i] = i/number_of_incriments
            plot_data_y[i] = t.update(t.initialise())
        
        # plot upon a graph and then show it
        plt.plot(plot_data_x, plot_data_y)
        plt.show()
            

def main():
    tt = TrafficTest()
    tt.run()
    
    ssp = SteadyStatePlot()
    ssp.run()
    
main()
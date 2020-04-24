from CP4 import Traffic
# modules required for our output
import matplotlib.pyplot as plt
import numpy as np


class TrafficTest(object):
    def run(self):
        t = Traffic(20, 0.7, 25)
        t.simulate()


class SteadyStatePlot(object):
    def run(self):
        # get input from user about how many increments we should use
        number_of_increments = int(input("Number of increments: \n"))
        # arrays for holding data for x/y axes
        plot_data_x = np.zeros(number_of_increments)
        plot_data_y = np.zeros(number_of_increments)
        # interate through all eventualities to get steady-state info for each
        for i in range(0, number_of_increments):
            t = Traffic(20, (i/number_of_increments), 50)
            plot_data_x[i] = i/number_of_increments
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

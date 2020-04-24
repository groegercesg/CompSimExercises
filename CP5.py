'''
CP5 - Orbital Motion
'''
# modules required for our simulation
import matplotlib.pyplot as plt
import math
import csv
from matplotlib.animation import FuncAnimation


class Simulation(object):
    # Creation of necessary Class Variables
    G = 6.67e-11
    DaySec = 24.0*60*60

    def __init__(self, myFileA, myFileB):
        # constructor, pulls relevant input parameters into the class

        # reading csv files
        with open(myFileA, 'r') as file:
            data_list_a = list(csv.reader(file))

        with open(myFileB, 'r') as file:
            data_list_b = list(csv.reader(file))

        # Mars
        self.xa = float((data_list_a[0])[0])
        self.ya = float((data_list_a[1])[0])

        self.xva = float((data_list_a[2])[0])
        self.yva = float((data_list_a[3])[0])

        self.ma = float((data_list_a[4])[0])

        # Phobos
        self.xb = float((data_list_b[0])[0])
        self.yb = float((data_list_b[1])[0])

        self.xvb = float((data_list_b[2])[0])
        self.yvb = math.sqrt((Simulation.G * self.ma)/(self.xb))
        # v_{2} = \sqrt{(G * m_{1})/(r_{12})}

        self.mb = float((data_list_b[4])[0])

        # Object Position Lists
        self.xalist = []
        self.yalist = []

        self.xblist = []
        self.yblist = []

    def TotalKE(self):
        # equation for Total KE
        # the sum of individual objects kinetic energies,
        # with KE = 1/2 * m * v^{2}
        # and so v^{2} term calculated using pythagoras of x and y velocities,
        # so square
        # root squared is just the underlying components
        return ((0.5 * self.ma * (self.xva**2 + self.yva**2)) +
                (0.5 * self.mb * (self.xvb**2 + self.yvb**2)))

    def runSim(self):
        # method to run the simulation of the objects

        t = 0.0
        dt = 0.001 * Simulation.DaySec  # timestep value

        # counter to track number of iterations, so as to print Total KE
        # at suitable intervals (roughly at every 10% of iterations)
        count = 0

        # loop
        while t < Simulation.DaySec:
            # orbital period is apparently 0.319 * DaySec,
            # but we'll roll with this for now
            # Compute force
            rx = self.xb - self.xa
            ry = self.yb - self.ya

            # modr3 being the denominator of our equation
            modr3 = (rx**2 + ry**2)**1.5

            fx = -(Simulation.G * self.ma * self.mb * rx)/(modr3)
            fy = -(Simulation.G * self.ma * self.mb * ry)/(modr3)

            # Update the quantities:
            # Phobos
            self.xvb += (fx*dt)/self.mb
            self.yvb += (fy*dt)/self.mb

            self.xb += self.xvb*dt
            self.yb += self.yvb*dt

            # Mars
            self.xva += -(fx*dt)/self.ma
            self.yva += -(fy*dt)/self.ma

            self.xa += self.xva*dt
            self.ya += self.yva*dt

            # increment t to move simulation forward
            t += dt

            # Save positions in lists,
            # these lists being for use in Animation classes methods
            self.xalist.append(self.xa)
            self.yalist.append(self.ya)

            self.xblist.append(self.xb)
            self.yblist.append(self.yb)

            # Code for printing KE at a suitable interval
            # (when count % 100 == 0)
            # this being, as in our simulation we have 1001 iterations,
            # 10 times
            # or at every 10% of the simulation
            count += 1
            if count % 100 == 0:
                print("Total Kinetic Energy: " + str(self.TotalKE()) + " J")


class Animation(object):
    def __init__(self, myXapos, myYapos, myXbpos, myYbpos):
        # constructor, pulls relevant inputs into the class
        self.xapos = myXapos
        self.yapos = myYapos
        self.xbpos = myXbpos
        self.ybpos = myYbpos

    def animate(self, i):
        # create 2 to be animated, using parameter i to move their position,
        # each with individual arrays
        self.patches[0].center = (self.xapos[i], self.yapos[i])
        self.patches[1].center = (self.xbpos[i], self.ybpos[i])
        return self.patches

    def display(self):
        fig = plt.figure()
        ax = plt.axes()

        # create an empty list for circles
        self.patches = []

        # create circles centred at initial position and then append
        # them to the list
        self.patches.append(plt.Circle((self.xapos[0], self.yapos[0]),
                                       250000, color='orange', animated=True))
        self.patches.append(plt.Circle((self.xbpos[0], self.ybpos[0]),
                                       250000, color='thistle', animated=True))

        # add circles to axes
        for i in range(0, len(self.patches)):
            ax.add_patch(self.patches[i])

        ax.axis('scaled')
        ax.set_xlim(-10000000, 10000000)
        ax.set_ylim(-10000000, 10000000)

        # animate the plot
        numFrames = len(self.xapos)

        # fig - the figure object we draw upon
        # self.animate - the function to call at each frame,
        # to generate the next position of things
        # numFrames - source of data to pass to func,
        # used to iterate through it
        # repeat=True - whether animation should repeat after sequence of
        # frames is completed
        # interval=20 - display interval
        # blit=True - blitting algorithm
        anim = FuncAnimation(  # noqa: F841
            fig, self.animate, numFrames, repeat=True, interval=20, blit=True)

        plt.show()


'''
def main():
    # Simulation
    s = Simulation('mars.csv', 'phobos.csv')
    s.runSim()

    # Animation
    a = Animation(s.xalist, s.yalist, s.xblist, s.yblist)
    a.display()

main()
'''

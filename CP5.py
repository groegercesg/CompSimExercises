'''
CP5 - Orbital Motion
'''
# modules required for our simulation
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

class Simulation(object):
    def runSim(self):
        # np.linspace - return evenly spaced numbers over a specified interval
        theta = np.linspace(0, 2*np.pi, 500)
        # self.[x/y]pos are arrays where each element has had the [cos/sin] function applied to it
        self.xpos = np.cos(theta)
        self.ypos = np.sin(theta)
            
class Animation(object):
    def __init__(self, myXpos, myYpos):
        # constructor, pulls relevant inputs into the class
        self.xpos = myXpos
        self.ypos = myYpos

    def animate(self, i):
        # update position of the circle
        self.patch.center = (self.xpos[i], self.ypos[i])
        return self.patch,
    
    def display(self):
        fig = plt.figure()
        ax = plt.axes()
        
        # create circle to be animated and add to plot at starting position
        self.patch = plt.Circle((self.xpos[0], self.ypos[0]), 0.1, color='b', animated=True)
        ax.add_patch(self.patch)
        
        ax.axis('scaled')
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
        
        # animate the plot
        numFrames = len(self.xpos)
        
        # fig - the figure object we draw upon
        # self.animate - the function to call at each frame, to generate the next position of things
        # numFrames - source of data to pass to func, used to iterate through it
        # repeat=True - whether animation should repeat after sequence of frames is completed
        # interval=20 - display interval
        # blit=True - blitting algorithm
        anim = FuncAnimation(fig, self.animate, numFrames, repeat=True, interval=20, blit=True)
        
        plt.show()
        
        
def main():
    # Simulation
    s = Simulation()
    s.runSim()
    
    # Animation
    a = Animation(s.xpos, s.ypos)
    a.display()
    
main()
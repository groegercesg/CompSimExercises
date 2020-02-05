'''
CP3 - Mandelbrot
'''
# modules required for our simulation
import matplotlib.pyplot as plt
import numpy as np

class Mandelbrot(object):
    def __init__(self, myIterations, myXMin, myXMax, myYMin, myYMax, myFilename):
        # constructor, pulls in all relevant details to the class
        self.Iterations = myIterations # number of iterations of mandelbrot method
        self.XMin = myXMin # xmin of sim and picture
        self.XMax = myXMax
        self.YMin = myYMin
        self.YMax = myYMax
        self.Filename = myFilename # name of file output
        
    def iterate(self, myComplex):
        # method to run the iteration of the mandelbrot
        # initial condition for z
        z = 0
        # n being out number of iterations, upper limit 255
        for n in range(1, self.Iterations):
            # mandelbrot function, with myComplex as our complex number input
            z = z**2 + myComplex
            #condition for tend to infinity and so a is not in mandelbrot set
            if abs(z) > 2:
                # return n to array (Z)
                return n
        #nan - Not a Number
        return np.nan
    
    def simulate(self):
        # method to operate the simulation of the mandelbrot 
        # arange - return evenly space values within given interval (0.002)
        # zeros - return array filled of zeroes of dimension len(Y) by len(X)
        X = np.arange(self.XMin, self.XMax, 0.002)
        Y = np.arange(self.YMin, self.YMax, 0.002) # 0.0001
        Z = np.zeros((len(Y), len(X)))

        # enumerate - allows looping over a array, and an automatic counter of it
        for iy, y in enumerate(Y):
            # progress message
            print(iy, "of", len(Y))
            for ix, x in enumerate(X):
                Z[iy,ix] = self.iterate(x + 1j * y)

        # Z - image data in scalar (data visualized usign a colormap)
        # plt.cm.prism - using colourmap of type prism (map scalar data to colours)
        # interpolation = 'none' - have blocks of colour and no artificial smoothing
        # extent - The bounding box in data coordinates that the image will fill, min()/max() lowest/largest value in an item
        plt.imshow(Z, cmap = plt.cm.prism, interpolation = 'none', extent = (X.min(), X.max(), Y.min(), Y.max()))
        # save image out as "mandelbrot_python.svg"
        plt.savefig(self.Filename+".svg")
        plt.show()

'''
def main():
    m = Mandelbrot(255, -2.025, 0.6, -1.125, 1.125, "mandelbrot_output")
    m.simulate()
    
main()
'''

# Feedback:
# Use matplotlib: meshgrid and np.vectorize() to speed up calculation (on 
# a method that encapsulates lines 41-46).
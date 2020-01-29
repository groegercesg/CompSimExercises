from CP2 import Decay

class DecayTest(object):
    def run(self):
        # decay constant, length of 2D array, timestep
        try:
            decaycons = float(input("What is the value of your decay constant: \n"))
            len2D = int(input("What is the length of the 2D array: \n"))
            timestep = float(input("What is the timestep: \n"))
            d = Decay(decaycons, len2D, timestep)
            d.decay_simulation()
        except:
            print("Data entered was not in correct format, please try again!")
            main()
          
        #d = Decay(0.02775,50,0.01)
        #d.decay_simulation()
        
def main():
    d1 = DecayTest()
    d1.run()
    
main()

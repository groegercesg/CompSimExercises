from CP5 import Simulation, Animation

class OrbitalMotionTest(object):
    def run(self):
        s = Simulation('mars.csv', 'phobos.csv')
        s.runSim()
        
        a = Animation(s.xalist, s.yalist, s.xblist, s.yblist)
        a.display()
        
def main():
    omt = OrbitalMotionTest()
    omt.run()
    
main()
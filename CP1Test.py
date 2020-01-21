from CP1 import Polynomial

class PolynomialTest(object):
    def run(self):
        # test outlined in Checkpoint requirements
        a = Polynomial([2,0,4,-1,0,6])
        b = Polynomial([-1,-3,0,4.5])
        c = Polynomial([0,8.0,-3.0,0,30])
        
        print("Calculates the order of Pa(x):")
        a.printPoly()
        
        print("Adds Pb(x) to Pa(x):")
        a.AddPoly("P(x) = 2 + 4x^2 - x^3 + 6x^5", "P(x) = -1 - 3x + 4.5x^3")
        
        print("Calculates the first derivative of Pa(x):")
        a.DerivePoly("P(x) = 2 + 4x^2 - x^3 + 6x^5")
        
        print("Calculates the antiderivative of this result:")
        c.IntegratePoly("P(x) = 8.0x - 3.0x^2 + 30.0x^4")
        
        
        # Pa(x) = 2 + 4x^2 - x^3 + 6x^5 , [2,0,4,-1,0,6]
        # Pb(x) = -1 - 3x + 4.5x^3 , [-1,-3,0,4.5]
        
            #g = Polynomial([-1,-3,0,4.5])
            #g.printPoly()
            #g.AddPoly("P(x) = -1 - 3x + 4.5x^3","P(x) = 2 + 4x^2 - x^3 + 6x^5")
            #g.DerivePoly("P(x) = -1 - 3x + 4.5x^3")
            #g.IntegratePoly("P(x) = -1 - 3x + 4.5x^3") 
        '''
        Calculates the order of Pa(x)
        Adds Pb(x) to Pa(x)
        Calculates the first derivative of Pa(x)
        Calculates the antiderivative of this result, i.e. the antiderivative of dPa(x)/dx. The constant of integration c should be set to c=2.
        '''

def main():
    p = PolynomialTest()
    p.run()
    '''
    p = Polynomial([2,0,4,-1,0,6])
    a_prin = "P(x) = 2 + 4x^2 - x^3 + 6x^5"
    b_prin = "P(x) = -1 - 3x + 4.5x^3"
    p.AddPoly(a_prin, b_prin)
    '''

main()
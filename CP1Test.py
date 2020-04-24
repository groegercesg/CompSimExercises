from CP1 import Polynomial


class PolynomialTest(object):
    def run(self):
        # test outlined in Checkpoint requirements
        a = Polynomial([2, 0, 4, -1, 0, 6])

        # tests to be run

        print("Calculates the order of Pa(x):")
        print(a.printPoly())

        print("Adds Pb(x) to Pa(x):")
        print(a.AddPoly("""P(x) = 2 + 4x^2 - x^3 + 6x^5",
                        "P(x) = -1 - 3x + 4.5x^3"""))

        print("Calculates the first derivative of Pa(x):")
        print(a.DerivePoly("P(x) = 2 + 4x^2 - x^3 + 6x^5"))

        print("Calculates the antiderivative of this result:")
        print(a.IntegratePoly(a.DerivePoly("P(x) = 2 + 4x^2 - x^3 + 6x^5")))

        '''
        Calculates the order of Pa(x)
        Adds Pb(x) to Pa(x)
        Calculates the first derivative of Pa(x)
        Calculates the antiderivative of this result,
        i.e. the antiderivative of dPa(x)/dx.
        The constant of integration c should be set to c=2.
        '''


def main():
    p = PolynomialTest()
    p.run()


main()

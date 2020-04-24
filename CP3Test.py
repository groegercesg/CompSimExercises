from CP3 import Mandelbrot


class MandelbrotTest(object):
    def run(self):
        m = Mandelbrot(255, -2.025, 0.6, -1.125, 1.125, "mandelbrot_output")
        m.simulate()


def main():
    mt = MandelbrotTest()
    mt.run()


main()
